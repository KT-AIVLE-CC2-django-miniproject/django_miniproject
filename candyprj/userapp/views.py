from audioop import reverse
from django.forms import NullBooleanField
from django.shortcuts import render,redirect
from django.contrib import messages #알람을 위한 임포트
from sqlalchemy import null
from .models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
def signup(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')
        birth = request.POST.get('birth')
        mail = request.POST.get('mail')
        m = User(id=id, pw=pw, name=name, birth=birth, mail=mail)
        m.save()
        return render(request, 'boardapp/login.html')
    else:
        return render(request, 'boardapp/signup.html')

# def profile(request):
#     profile = User.objects.get(id = 'abc')
#     return render(request, 'userapp/profile.html',{'profile':profile})

def profile(request):
    # profile = User.objects.get(id = 'abc')
    id = request.session.get('id')
    profile = User.objects.get(id = id)
    return render(request, 'userapp/profile.html',{'profile':profile})


def update(request):
    # update = User.objects.get(id = 'abc')
    id = request.session.get('id')
    update = User.objects.get(id = id)
    new = User.objects.get(id = id)
    if request.method == "POST":
        
        # update.pw = request.POST.get('pw')
        # update.name = request.POST.get('name')
        # update.birth = request.POST.get('birth')
        # update.mail = request.POST.get('mail')
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

        # if update.pw !="" and update.name !="" and update.birth !="" and update.mail !="":
        #     update.save()                 //모든 값이 입력됐을 경우만 db에 저장
        # print(result)
        # return HttpResponseRedirect(reverse('profile'))
        return render(request, 'userapp/new_profile.html')

    else:
        return render(request, 'userapp/update.html', {'update':update,'new':new})



def login(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        try:
            m = User.objects.get(id=id, pw=pw)
        except User.DoesNotExist as e:
            messages.warning(request, "로그인 실패!")
            return render(request, 'boardapp/login.html')

        else:
            request.session['id'] = m.id
            request.session['name'] = m.name
            
        # return render(request,'boardapp/main.html')
        return redirect('../../board/home')
    else:
        return render(request, 'boardapp/login.html')

def logout(request):
    # del request.session['id'] # 개별 삭제
    # del request.session['name'] # 개별 삭제
    request.session.flush() # 전체 삭제
    # return render(request,'boardapp/main.html')
    return redirect('../../board/home')


# def profile(request):
#     id = request.session.get('id')
#     profile = User.objects.get(id = id)
#     return render(request, 'userapp/profile.html',{'profile':profile})

