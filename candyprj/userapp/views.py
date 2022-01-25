from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
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

# from .forms import UserUpdateForm
# def update(request):
#     if request.method == "POST":
#         form = UserUpdateForm(request.POST, instance=request.user)  # 이게 없으면 수정할 때마다 새로운 계정을 만든다.
#         if form.is_valid():
#             form.save()  # 폼값을 불러오고 저장
#             return redirect('user/profile/')
#     else:
#         form = UserUpdateForm(instance=request.user)
#     return render(request, 'userapp/update.html', {'form': form})




  
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
            

        # return render(request,'boardapp/main.html')
        return redirect('../../board/main')
    else:
        return render(request, 'userapp/login.html')

def logout(request):
    # del request.session['id'] # 개별 삭제
    # del request.session['name'] # 개별 삭제
    request.session.flush() # 전체 삭제
    # return render(request,'boardapp/main.html')
    return redirect('../../board/main')

