from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django import forms
from django.conf import settings
import json
import datetime
from book.models import Book
from tag.models import Booktag
import json
import urllib2


def index(request):
    return HttpResponse(json.dumps('hello world!'), content_type="application/json")

@cache_page(60 * 60 * 24)
def tag_list(request):
    data = json.load(urllib2.urlopen('http://192.168.8.103:27080/weishuku/booktag/_find'))
    return HttpResponse(json.dumps(data), content_type="application/json")


def taged_book(request, tag_id):
    context = dict()
    id_list = Booktag.objects.filter(tagid=tag_id)
    book_list = []
    for id in id_list:
        book = Book.objects.filter(id=id.bookid)[0]
        book_list.append(book)
    context['book_list'] = book_list
    return render(request, 'tag/booklist.html', context)