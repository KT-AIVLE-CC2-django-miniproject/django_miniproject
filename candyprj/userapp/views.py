from audioop import reverse
from django.forms import NullBooleanField
from django.shortcuts import render,redirect
from numpy import empty
from sqlalchemy import null
from .models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')
        birth = request.POST.get('birth')
        mail = request.POST.get('mail')
        m = User(id=id, pw=pw, name=name, birth=birth, mail=mail)
        m.save()

        return redirect('../../user/login')     

    else:
        return render(request, 'userapp/signup.html')


def profile(request):
    # profile = User.objects.get(id = 'abc')
    id = request.session.get('id')
    profile = User.objects.get(id = id)
    return render(request, 'userapp/profile.html',{'profile':profile})


def update(request):
    id = request.session.get('id')
    update = User.objects.get(id = id)
    new = User.objects.get(id = id)
    if request.method == "POST":

        update.file = request.FILES.get('file') 
        if update.file == None:
            update.file = new.file
        else :
            update.file = update.file
        
        update.pw = request.POST.get('pw')
        if update.pw =='':
            update.pw = new.pw
        else :
            update.pw = update.pw
        
        update.name = request.POST.get('name')
        if update.name =='':
            update.name = new.name
        else :
            update.name = update.name
        
        update.birth = request.POST.get('birth')
        if update.birth =='':
            update.birth = new.birth
        else :
            update.birth = update.birth

        update.mail = request.POST.get('mail')
        if update.mail =='':
            update.mail = new.mail
        else :
            update.mail = update.mail
        
       
        update.save()


        return render(request, 'userapp/new_profile.html')

    else:
        return render(request, 'userapp/update.html', {'update':update,'new':new})

# def img_show(request):
#     id = request.session.get('id')
#     image = User.objects.get(id = id)
#     uploadFile = image.objects.get(id=id)
#     return render(
#         request, 'userapp/profile.html',
#         {'uploadFile': uploadFile})


def login(request):
    
    if request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        try:
            m = User.objects.get(id=id, pw=pw)
        except User.DoesNotExist as e:
            messages.add_message(request, messages.INFO, '아이디 비밀번호를 확인하세요!')
            return render(request, 'userapp/login.html')

        else:
            request.session['id'] = m.id
            request.session['name'] = m.name
            
        return redirect('../../board/home')
    else:
        return render(request, 'userapp/login.html')


def logout(request):
    # del request.session['id'] # 개별 삭제
    # del request.session['name'] # 개별 삭제
    request.session.flush() # 전체 삭제
    # return render(request,'boardapp/main.html')
    return redirect('../../board/main')


# def profile(request):
#     id = request.session.get('id')
#     profile = User.objects.get(id = id)
#     return render(request, 'userapp/profile.html',{'profile':profile})

def userinfo(request, id):
    user = User.objects.get(id=id)

    return render(request, 'userapp/profile.html',{'profile':user})

