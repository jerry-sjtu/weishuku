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


class City(models.Model):
    cityid = models.IntegerField(db_column='CityID', primary_key=True) # Field name made lowercase.
    cityname = models.CharField(db_column='CityName', max_length=45, blank=True) # Field name made lowercase.
    cityenname = models.CharField(db_column='CityEnName', max_length=45, blank=True) # Field name made lowercase.
    cityabbrcode = models.CharField(db_column='CityAbbrCode', max_length=45, blank=True) # Field name made lowercase.
    newcityabbrcode = models.CharField(db_column='NewCityAbbrCode', max_length=45, blank=True) # Field name made lowercase.
    cityareacode = models.CharField(db_column='CityAreaCode', max_length=45, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'City'


    def all_cities(self):
        q = City.objects.values('cityid', 'cityname')
        r_list = list()
        for r in q:
            r_list.append((r['cityid'], r['cityname']))
        return r_list