from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
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

def profile(request):
    profile = User.objects.get(id = 'abc')
    return render(request, 'userapp/profile.html',{'profile':profile})







  