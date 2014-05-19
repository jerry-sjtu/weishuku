# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
import json
import urllib2
from book.models import Book
from member.models import Dper, CityArea, City
from tag.models import Tag
from message.models import Message
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index_page(request, page):
    context = dict()
    #get the city name
    if request.user.id != None:
        context['city_id'] = Dper.objects.get(user_id=request.user.id).city
        context['city_name'] = City.objects.get(cityid=context['city_id']).cityname

    flag = False
    if request.path == None or len(request.path) == 1:
        if request.user.id == None:
            city_en_name = "shanghai"
            flag = True
    else:
        city_en_name = request.path[1:-1]
        flag = True

    if flag == True:
        area_obj = CityArea()
        context['city_name'] = area_obj.convert_city_name(city_en_name)
        context['city_id'] = area_obj.get_city_id(city_en_name)


    context['tag_list'] = [tag for tag in Tag.objects.all()][0:10]
    is_login = request.user.is_authenticated()
    context['is_login'] = is_login
    if is_login:
        context['username'] = request.user.username
        context['msg_num'] = Message.objects.filter(targetid=request.user.id, status=0).count()

    book_list = [book for book in Book.objects.filter(city=context['city_id'])]
    for b in book_list:
        name = User.objects.filter(id=b.ownerid)[0].username
        dpers = [d for d in Dper.objects.filter(id=b.ownerid)]
        department = ''
        if len(dpers) > 0:
            department = dpers[0].department
        b.username = name
        b.position = department
    book_list = Paginator(book_list, 3)
    context['book_list'] = book_list.page(int(page))
    return render(request, 'default/home.html', context)

def index(request):
    return index_page(request, 1)