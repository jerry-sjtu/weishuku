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
    cityname = models.CharField(db_column='CityName', max_length=45, blank=True) # Field name made lowercase.
    cityenname = models.CharField(db_column='CityEnName', max_length=45, blank=True) # Field name made lowercase.
    cityabbrcode = models.CharField(db_column='CityAbbrCode', max_length=45, blank=True) # Field name made lowercase.
    newcityabbrcode = models.CharField(db_column='NewCityAbbrCode', max_length=45, blank=True) # Field name made lowercase.
    cityareacode = models.CharField(db_column='CityAreaCode', max_length=45, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'City'