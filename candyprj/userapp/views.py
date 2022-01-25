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

# from django.shortcuts import redirect
# from .forms import ProfileForm
# def update(request):
#     if request.method == "POST":
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             """
#             현재 유저의 프로필을 가져오고
#             받은 값으로 프로필을 갱신한다.
#             """
#             old_profile = request.user.profile
#             old_profile.pw = form.cleaned_data['pw']
#             old_profile.name = form.cleaned_data['name']
#             old_profile.save()
#             return redirect('profile')
#     elif request.method == "GET":
#         form = ProfileForm(instance=request.user.profile)
#         return render(request, 'user/profile_form.html', {
#             'form': form,
#         })



  
def login(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        try:
            m = User.objects.get(id=id, pw=pw)
        except User.DoesNotExist as e:
            return HttpResponse('로그인 실패')
        else:
            request.session['id'] = m.id
            request.session['name'] = m.name

        return render(request,'boardapp/main.html')
    else:
        return render(request, 'userapp/login.html')

def logout(request):
    del request.session['id'] # 개별 삭제
    del request.session['name'] # 개별 삭제
    request.session.flush() # 전체 삭제
    return render(request,'boardapp/main.html')


