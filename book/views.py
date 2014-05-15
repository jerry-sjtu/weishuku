# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django import forms
from django.conf import settings
import json
from django.db.models import Q

import json
import datetime

from book.models import Book, Borrowrel
from book.forms import BookForm
from member.models import Dper
from tag.models import Tag, Booktag
from message.models import Message
from url_tool import parse_book_by_isbn

def index(request):
    return HttpResponse(json.dumps('hello world!'), content_type="application/json")

@cache_page(60 * 60 * 24)
def book_list(request):
    is_login = request.user.is_authenticated()
    q = Book.objects.all()
    book_list = [(item.title,item.isbn) for item in q]
    return HttpResponse(json.dumps(book_list), content_type="application/json")

@login_required
def library(request):
    context = dict()
    q = Book.objects.filter(ownerid=request.user.id)
    book_list = [item for item in q]

    borrow_list = list()
    for rel in Borrowrel.objects.filter(borrower=request.user.id):
        book = Book.objects.filter(id=rel.bookid)[0]
        book.status = rel.status
        borrow_list.append(book)

    return_list = list()
    for rel in Borrowrel.objects.filter(owner=request.user.id):
        book = Book.objects.filter(id=rel.bookid)[0]
        book.status = rel.status
        return_list.append(book)

    context['book_list'] = book_list
    context['is_login'] = request.user.is_authenticated()
    context['username'] = request.user.username
    context['msg_num'] = Message.objects.filter(targetid=request.user.id, status=0).count()
    context['book_num'] = len(book_list)
    context['borrow_num'] = len(borrow_list)
    context['return_num'] = len(return_list)
    context['return_list'] = return_list
    context['borrow_list'] = borrow_list
    return render(request, 'book/library.html', context)

@login_required
def add_book(request):
    context = dict()
    if request.method == 'POST':
        if 'url' in request.POST:
            url = request.POST['url']    
            context = parse_book_by_isbn(url)
            return render(request, 'book/add.html', context)
        if 'isbn' in request.POST:
            isbn = request.POST['isbn']
            context = parse_book_by_isbn(isbn)
            book = Book()
            book.title = context['title']
            book.publisher = context['publisher']
            book.isbn = context['isbn']
            book.url = context['url']
            book.ispersonal = int(True)
            book.ownerid = request.user.id
            book.summary = context['summary']
            book.price = context['price']
            book.numraters = 0
            book.averageRate = 3
            book.created_date = datetime.datetime.now()
            book.updated_date = datetime.datetime.now()
            book.author = context['author'][0]
            book.pubdate = context['pubdate']
            book.ispublic = int(True)
            book.imgurl = context['images']
            book.save()

            #save tags of book
            for val in context['tags']:
                tag = Tag()
                tag.value = val
                tag.createdate = datetime.datetime.now()
                tag.save()
                rel = Booktag()
                rel.tagid = tag.id
                rel.bookid = book.id
                rel.save()
            return redirect('/book/library', context)
    else:    
        form = BookForm()
        context['form'] = form
        return render(request, 'book/add.html', context)

def info_book(request, id):
    context = dict()
    context['is_login'] = request.user.is_authenticated()
    if request.user.is_authenticated():
        context['username'] = request.user.username
    book = Book.objects.filter(id=id)[0]
    context['book'] = book
    context['userid'] = request.user.id
    context['is_own'] = (book.ownerid == request.user.id)

    context['tags'] = []
    for tagid in [rel.tagid for rel in Booktag.objects.filter(bookid=id)]:
        context['tags'].append(Tag.objects.filter(id=tagid)[0].value)
    return render(request, 'book/detail.html', context)

@login_required
def del_book(request):
    pass
    
@login_required
def update_book(request):
    pass

@login_required
def borrow_book(request):
    if request.method == 'POST' and 'bookid' in request.POST:
        borrower = request.user.id
        book = Book.objects.filter(id=request.POST['bookid'])[0]
        ownerid = book.ownerid

        msg = Message()
        msg.originid = borrower
        msg.targetid = ownerid
        msg.status = 0
        msg.createdate = datetime.datetime.now()
        msg.content = request.POST['message'] 
        msg.handler = '/book/library/'
        msg.save()

        rel = Borrowrel()
        rel.bookid = book.id
        rel.owner = ownerid
        rel.borrower = borrower
        rel.createdate = datetime.datetime.now()
        rel.status = 0
        rel.messageid = msg.id
        rel.save()
        return redirect('/book/library/')

@login_required
def approve_borrow(request, bookid):
    rel = Borrowrel.objects.filter(bookid=bookid)[0]
    rel.status = 2
    rel.save()
    return redirect('/book/library/')

@login_required
def refuse_borrow(request, bookid):
    rel = Borrowrel.objects.filter(bookid=bookid)[0]
    rel.status = 1
    rel.save()
    return redirect('/book/library/')


@login_required
def return_book(request, id):
    context = dict()
    context['is_login'] = request.user.is_authenticated()
    if request.user.is_authenticated():
        context['username'] = request.user.username
    q = Borrowrel.objects.filter(bookid=id, borrower=request.user.id)    
    q[0].delete()
    return redirect('/book/library/')



def search_book(request, keyword):
    print 'keyword:%s' % keyword
    book_list = Book.objects.filter(
        Q(title__contains=keyword) | Q(author__contains=keyword),
    )
    html_list = format_book_list(book_list)
    return HttpResponse(html_list, content_type='application/html')


def format_book_list(book_list):
    base_html = u'''
                <div class="col-md-3 libray_book">
                    <a href="/book/%s">
                        <img src="%s" class="img-polaroid book_img">
                        <h4>%s</h4>
                        <h5>拥有者:%s</h5>
                        <h5>位置:%s</h5>
                    </a>
                </div>
    '''
    html_list = ""
    for book in book_list:
        user = User.objects.filter(id=book.ownerid)
        dper = Dper.objects.filter(id=book.ownerid)
        html_list += base_html % (book.id, book.imgurl, book.title, user[0].username, dper[0].department)
    return html_list