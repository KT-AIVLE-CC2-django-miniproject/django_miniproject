from django.db import models
# Create your models here.
class Board(models.Model):
    '''
    '''
    id = models.CharField(max_length=20 ,primary_key=True)
    pw = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    birth = models.IntegerField()
    mail = models.CharField(max_length=45)
    reportCnt = models.IntegerField(default=0)
