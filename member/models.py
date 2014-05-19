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

class Province(models.Model):
    provinceid = models.IntegerField(db_column='ProvinceID', primary_key=True) # Field name made lowercase.
    areaid = models.IntegerField(db_column='AreaID') # Field name made lowercase.
    provincename = models.CharField(db_column='ProvinceName', max_length=10) # Field name made lowercase.
    provinceorderid = models.IntegerField(db_column='ProvinceOrderID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ZS_ProvinceList'

class City(models.Model):
    cityid = models.IntegerField(db_column='CityID', primary_key=True) # Field name made lowercase.
    cityname = models.CharField(db_column='CityName', max_length=20) # Field name made lowercase.
    provinceid = models.IntegerField(db_column='ProvinceID', blank=True, null=True) # Field name made lowercase.
    province = models.ForeignKey(Province, db_column='ProvinceID', to_field='provinceid')
    cityorderid = models.IntegerField(db_column='CityOrderID') # Field name made lowercase.
    isactivecity = models.TextField(db_column='IsActiveCity', blank=True) # Field name made lowercase. This field type is a guess.
    istrackcity = models.TextField(db_column='IsTrackCity', blank=True) # Field name made lowercase. This field type is a guess.
    dailysearchcount = models.IntegerField(db_column='DailySearchCount') # Field name made lowercase.
    cityenname = models.CharField(db_column='CityEnName', max_length=15, blank=True) # Field name made lowercase.
    cityareacode = models.CharField(db_column='CityAreaCode', max_length=10, blank=True) # Field name made lowercase.
    cityabbrcode = models.CharField(db_column='CityAbbrCode', max_length=3, blank=True) # Field name made lowercase.
    isjifencity = models.TextField(db_column='IsJifenCity') # Field name made lowercase. This field type is a guess.
    ispromocity = models.TextField(db_column='IsPromoCity') # Field name made lowercase. This field type is a guess.
    ismulticategorycity = models.TextField(db_column='IsMultiCategoryCity') # Field name made lowercase. This field type is a guess.
    tuangouflag = models.IntegerField(db_column='TuanGouFlag') # Field name made lowercase.
    citylevel = models.IntegerField(db_column='CityLevel', blank=True, null=True) # Field name made lowercase.
    glat = models.FloatField(db_column='GLat') # Field name made lowercase.
    glng = models.FloatField(db_column='GLng') # Field name made lowercase.
    gzoom = models.IntegerField(db_column='GZoom') # Field name made lowercase.
    directurl = models.CharField(db_column='DirectURL', max_length=100, blank=True) # Field name made lowercase.
    isnavurl = models.TextField(db_column='IsNavUrl', blank=True) # Field name made lowercase. This field type is a guess.
    isbusinesscity = models.TextField(db_column='IsBusinessCity') # Field name made lowercase. This field type is a guess.
    deliverflag = models.IntegerField(db_column='DeliverFlag') # Field name made lowercase.
    newcityabbrcode = models.CharField(db_column='NewCityAbbrCode', max_length=3, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ZS_CityList'


    def all_cities(self):
        q = City.objects.filter(citylevel__in=[1,2,3]).values('cityid', 'cityname')
        r_list = list()
        for r in q:
            r_list.append((r['cityid'], r['cityname']))
        return r_list


class CityArea(object):
    area_d = {1 : '华北东北地区', 2 : '华北东北地区',  3:'华东地区', 4:'华南地区', 5:'中西部地区'}

    def get_area(self, id):
        if id in self.area_d:
            return self.area_d[id]
        return '其它地区'

    def convert_city_name(self, city_en_name):
        q_list = [item for item in City.objects.filter(cityenname=city_en_name)]
        if len(q_list) == 0:
            return '上海'
        return q_list[0].cityname

    def get_city_id(self, city_en_name):
        q_list = [item for item in City.objects.filter(cityenname=city_en_name)]
        if len(q_list) == 0:
            return 1
        return q_list[0].cityid
