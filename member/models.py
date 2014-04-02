#encoding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Dper(models.Model):
    """添加帐号信息相关、作扩展用"""
    user = models.OneToOneField(User)
    sex = models.IntegerField()
    phone = models.CharField(max_length=20, null=True, default='')
    city = models.IntegerField()
    department = models.CharField(max_length=50, null=True, default='')

    class Meta:
        db_table = 'Dper'

    def __unicode__(self):
        return self.user.username
