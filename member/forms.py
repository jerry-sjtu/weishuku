# -*- coding: utf-8 -*-
from django import forms
import re
from django.contrib.auth.models import User
from member.models import City


def is_email(email):
    p = re.compile('[a-z0-9A-Z_]+@[a-z0-9]+\.com')
    return p.match(email) != None

def validate_user(username):
    user = User.objects.filter(username=username)
    if len(user) > 0:
        return False
    return True


class LoginForm(forms.Form):
    account = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    remember = forms.BooleanField(required=False)
    next =  forms.CharField(max_length=100)

class RegisterForm(forms.Form):
    account = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    repeat_password = forms.CharField(max_length=100)
    remember = forms.BooleanField(required=False)
    department = forms.CharField(max_length=100, required=False)
    city_obj = City()
    city_list = forms.ChoiceField(city_obj.all_cities())
    sex = forms.IntegerField()
    phone = forms.CharField(max_length=100, required=False)
    email = forms.CharField(max_length=100)


    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("repeat_password")

        if password1 == None or password2 == None or password1 != password2:
            #self.add_error('password', '密码不一致')
            raise forms.ValidationError('密码不一致')
        if cleaned_data.get("email") == None:
            raise forms.ValidationError('邮箱不能为空')
        if not is_email(cleaned_data.get("email")):
            raise forms.ValidationError('邮箱格式不正确')
        if not validate_user(cleaned_data.get("account")):
            raise forms.ValidationError('用户名已经被注册')
        return cleaned_data