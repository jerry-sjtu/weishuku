# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
import json
import urllib2
from book.models import Book
from member.models import Dper
from tag.models import Tag
from message.models import Message
from django.contrib.auth.models import User

def index(request):
    context = dict()
    #tag_data = json.load(urllib2.urlopen('http://192.168.8.103:27080/weishuku/booktag/_find'))
    #tag_list = list()
    #for item in tag_data['results']:
    #    tag_list.append(item['name'])
    context['tag_list'] = [tag.value for tag in Tag.objects.all()][0:10]
    is_login = request.user.is_authenticated()
    context['is_login'] = is_login
    if is_login:
        context['username'] = request.user.username
        context['msg_num'] = Message.objects.filter(targetid=request.user.id, status=0).count()
    book_list = [book for book in Book.objects.all()]
    for b in book_list:
        name = User.objects.filter(id=b.ownerid)[0].username
        department = Dper.objects.filter(id=b.ownerid)[0].department
        b.username = name
        b.position = department
    context['book_list'] = book_list
    return render(request, 'default/home.html', context)

