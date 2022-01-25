from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
from django.contrib.auth import  login
# from django.contrib.auth.models import User
# from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')
        birth = request.POST.get('birth')
        mail = request.POST.get('mail')
        m = User(id=id, pw=pw, name=name, birth=birth, mail=mail)

        m.save()
        return HttpResponse(
            '가입 완료<br>%s %s %s %s %s ' % (id, pw, name, birth, mail))
    else:
        return render(request, 'userapp/signup.html')


def login(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        try:
            m = User.objects.get(id=id, pw=pw)
        except User.DoesNotExist as e:
            return HttpResponse('로그인 실패')
        return HttpResponse('로그인 성공')
    else:
        return render(request, 'userapp/login.html')

# def login(request):
#     if request.method == "POST":
#        id = request.POST.get('id')
#        pw = request.POST.get('pw')
#        user=auth.authenticate(request,id=id,pw=pw)
#        if user is not None:
#            auth.login(request, user)
#            return HttpResponse('로그인 성공')
#        else:
#            return HttpResponse('로그인 실패')
#     else:
#         return render(request, 'userapp/login.html')
        