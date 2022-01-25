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

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    