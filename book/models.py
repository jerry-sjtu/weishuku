from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1024L)
    publisher = models.CharField(max_length=1024L, blank=True)
    isbn = models.CharField(max_length=20L)
    url = models.CharField(max_length=256L, blank=True)
    ispersonal = models.IntegerField(db_column='isPersonal') # Field name made lowercase.
    ownerid = models.IntegerField()
    summary = models.CharField(max_length=4096L, blank=True)
    price = models.FloatField(null=True, blank=True)
    numraters = models.CharField(max_length=45L, db_column='numRaters', blank=True) # Field name made lowercase.
    averagerate = models.IntegerField(null=True, db_column='averageRate', blank=True) # Field name made lowercase.
    created_date = models.DateTimeField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    borrowdate = models.DateTimeField(null=True, blank=True)
    author = models.CharField(max_length=128L, blank=True)
    authorinfo = models.CharField(max_length=4096L, null=True, blank=True)
    catelog = models.CharField(max_length=4096L, null=True, blank=True)
    pubdate = models.CharField(max_length=45L, blank=True)
    ispublic = models.IntegerField(null=True, db_column='isPublic', blank=True) # Field name made lowercase.
    imgurl = models.CharField(max_length=256L, db_column='ImgURL', blank=True) # Field name made lowercase.
    city = models.IntegerField()
    status = models.IntegerField()
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
    agreedate = models.DateTimeField(db_column='AgreeDate', blank=True, null=True) # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True) # Field name made lowercase.
    class Meta:
        db_table = 'BorrowRel'

