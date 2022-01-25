from django.db import models
from sqlalchemy import ForeignKey
from userapp.models import User
# Create your models here.
class Board(models.Model):
    '''
    postNum : 게시글번호(PK)
    title : 제목
    content : 내용
    id: 작성자 (FK)
    pub_date: 배포일
    recuritment = 모집중 or 모집완료
    '''
    postNum = models.AutoField(primary_key=True)
    id = models.ForeignKey("userapp.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length= 1000)
    pub_date = models.DateTimeField()
    # recuritment = models.BooleanField()

    def __str__(self):
        return self.title
class Reply(models.Model):
    '''
    repNum : 댓글번호(PK)
    postNum : 게시글번호(FK)
    id : 작성자(FK)
    comment : 댓글내용
    rep_date : 작성일
    '''
    repNum = models.AutoField(primary_key=True)
    postNum = models.ForeignKey(Board, on_delete=models.CASCADE)
    id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    rep_date = models.DateTimeField()

    def __str__(self):
        return self.comment