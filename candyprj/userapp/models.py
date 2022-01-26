from django.db import models
# Create your models here.
class User(models.Model):
    '''
    id : 회원아이디(PK)
    pw : 비밀번호
    name : 이름
    birth : 생년월일
    mail : 이메일
    reportCnt : 신고누적횟수
    '''
    id = models.CharField(max_length=20 ,primary_key=True)
    pw = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    birth = models.CharField(max_length=45)
    mail = models.CharField(max_length=45)
    reportCnt = models.IntegerField(default=0)

