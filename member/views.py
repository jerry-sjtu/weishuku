from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required

from member.forms import LoginForm, RegisterForm
from member.models import Dper, City, Province, CityArea
import json



def my_login(request):
    context = dict()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            account = form.cleaned_data['account']
            password = form.cleaned_data['password']
            remember = form.cleaned_data['remember']
            next = form.cleaned_data['next']
            user = authenticate(username=account, password=password)
            if user is not None:
                login(request, user)
                #print 'user of session:%s' % (request.user.is_authenticated())
                #print 'user of name:%s ' % request.user.username
                #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                return redirect(next, context)
            else:
                context['form'] = LoginForm()
                context['next'] = next
                return render(request, 'member/login.html', context)
    else:
        next = '/'
        if 'next' in request.GET:
            next = request.GET['next']
        context['form'] = LoginForm()
        context['next'] = next
    return render(request, 'member/login.html', context)

@login_required
def my_logout(request):
    logout(request)
    return redirect('/')

def register(request):
    context = dict()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print 'form'
        if form.is_valid():
            account = form.cleaned_data['account']
            password = form.cleaned_data['password']
            remember = form.cleaned_data['remember']
            phone = form.cleaned_data['phone']

            department = form.cleaned_data['department']
            city = form.cleaned_data['city_list']
            sex = form.cleaned_data['sex']
            user = User.objects.create_user(username=account, password=password)
            user = authenticate(username=account, password=password)
            dper = Dper.objects.create(user=user, city=city, department=department, phone=phone, sex=sex)
            if user is not None:
                dper.save()
                login(request, user)
            return redirect('/', context)
        else:
            context['form'] = form
            return render(request, 'member/register.html', context)
    else:
        context['form'] = RegisterForm()
        return render(request, 'member/register.html', context)


def city_list_with_region(request):
    area_obj = CityArea()
    area_d = dict()
    q = City.objects.filter(citylevel__in=[1,2,3])
    for item in q:
        try:
            area_name = area_obj.get_area(item.province.areaid)
            if area_name not in area_d:
                area_d[area_name] = list()
            area_d[area_name].append((item.cityid, item.cityenname, item.cityname))
        except Province.DoesNotExist:
            pass
    #return HttpResponse(json.dumps(area_d), content_type="application/json")
    context = dict()
    context['area_d'] = area_d
    return render(request, 'member/citylist.html', context)