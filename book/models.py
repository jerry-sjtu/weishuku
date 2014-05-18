from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128L)
    publisher = models.CharField(max_length=128L, blank=True)
    isbn = models.CharField(max_length=13L)
    url = models.CharField(max_length=128L, blank=True)
    ispersonal = models.IntegerField(db_column='isPersonal') # Field name made lowercase.
    ownerid = models.IntegerField()
    summary = models.CharField(max_length=1024L, blank=True)
    price = models.FloatField(null=True, blank=True)
    numraters = models.CharField(max_length=45L, db_column='numRaters', blank=True) # Field name made lowercase.
    averagerate = models.IntegerField(null=True, db_column='averageRate', blank=True) # Field name made lowercase.
    created_date = models.DateTimeField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    borrowdate = models.DateTimeField(null=True, blank=True)
    author = models.CharField(max_length=128L, blank=True)
    pubdate = models.CharField(max_length=45L, blank=True)
    ispublic = models.IntegerField(null=True, db_column='isPublic', blank=True) # Field name made lowercase.
    imgurl = models.CharField(max_length=128L, db_column='ImgURL', blank=True) # Field name made lowercase.
    city = models.IntegerField()
    bookcount = models.IntegerField()
    class Meta:
        db_table = 'Book'

    def __unicode__(self):
        return self.title


class Borrowrel(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id') # Field name made lowercase.
    bookid = models.IntegerField(db_column='BookID') # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner') # Field name made lowercase.
    borrower = models.IntegerField(db_column='Borrower') # Field name made lowercase.
    status = models.IntegerField(db_column='Status') # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate') # Field name made lowercase.
    deldate = models.DateTimeField(db_column='DelDate') # Field name made lowercase.
    messageid = models.IntegerField(db_column='MessageID') # Field name made lowercase.
    class Meta:
        db_table = 'BorrowRel'

class City(models.Model):
    cityid = models.IntegerField(db_column='CityID', primary_key=True) # Field name made lowercase.
    cityname = models.CharField(db_column='CityName', max_length=20) # Field name made lowercase.
    provinceid = models.IntegerField(db_column='ProvinceID', blank=True, null=True) # Field name made lowercase.
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

class Province(models.Model):
    provinceid = models.IntegerField(db_column='ProvinceID', primary_key=True) # Field name made lowercase.
    areaid = models.IntegerField(db_column='AreaID') # Field name made lowercase.
    provincename = models.CharField(db_column='ProvinceName', max_length=10) # Field name made lowercase.
    provinceorderid = models.IntegerField(db_column='ProvinceOrderID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ZS_ProvinceList'