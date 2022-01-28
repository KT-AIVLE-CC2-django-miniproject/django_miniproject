from django.db import models
from sqlalchemy import ForeignKey
from userapp.models import User
# Create your models here.
class Board(models.Model):
    '''
    postNum : 게시글번호(PK)
    title : 제목
    content : 내용
    id : 작성자 (FK)
    pub_date : 배포일
    imgfile : 이미지파일
    '''
    postNum = models.AutoField(primary_key=True)
    id = models.ForeignKey("userapp.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length= 1000)
    pub_date = models.DateTimeField()
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
        return self.comment, self.id


#########################################################기업별 면접 공유 게시판

class Topic(models.Model):
    message = models.TextField(max_length=5000,null=True) #content
    subject = models.CharField(max_length=255) #title
    last_updated =  models.DateField(auto_now_add=True, null=True)
    writter = models.ForeignKey("userapp.User", related_name='topics',on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.writter    


class Replys(models.Model):
    '''
    message 댓글내용
    created_at -댓글 작성일시
    created_by 댓글 쓴사람
    updated at 댓글 수정일시
    updated by 댓글 수정한사람
    
    '''
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now=True)
    created_by= models.ForeignKey("userapp.User", null=True, related_name='posts',on_delete=models.CASCADE)
    updated_at = models.DateField(null = True)
    updated_by=  models.ForeignKey("userapp.User",null=True,related_name='+',on_delete=models.CASCADE)
    # topic = models.ForeingKey('Topic')

    # topic =  Otpic.objexts.get(id=topicid)
    # replies  = topic.repliy_set.all()
    # render (template, { topic, replies})

    # {% for r in replies %}
    #     {{r.body}}
    # {%endfor %}