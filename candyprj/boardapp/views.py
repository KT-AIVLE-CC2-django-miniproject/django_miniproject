from email.policy import default
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse
from django.core.paginator import Paginator
from matplotlib.pyplot import title
from userapp.models import User

from .models import Board

# from userapp.views import ss

#기본페이지
# def index(request):
#     return render(request, 'boardapp/index.html', {'title':'data'})

def home(request):
    board = Board.objects.all().order_by('-postNum')[:5]
    return render(request, 'boardapp/home.html', {'title':'home', 'board':board})

def board(request):
    return render(request, 'boardapp/board.html', {'title':'board'})  


#######################################################################

def index(request): #게시글 목록
    all_boards = Board.objects.all()
    paginator = Paginator(all_boards, 10)
    page = int(request.GET.get('page',1))
    board_list = paginator.get_page(page)

    board = Board.objects.all().order_by('-postNum')[:5]
    
    return render(request, 'boardapp/index.html', {'title':'Board List', 'board_list': board_list, 'board':board})

def detail(request, postNum): #게시글 제목 선택시 상세 페이지로 이동
    board = Board.objects.get(postNum=postNum)
    return render(request, 'boardapp/detail.html', {'boardapp': board})

def write(request): #게시글 목록에서 글쓰기 버튼 클릭 시 쓰기 페이지로 이동
    return render(request, 'boardapp/write.html')

def write_board(request): #쓰기 페이지에서 글 등록시 submit 처리
    # uid = ss.GET.get('ses_id')
    uid = request.session['id']
    uid = User.objects.get(id = uid)

    cid = request.session['id']
    cid = Board.objects.get(id=cid)
    
    b = Board(id = uid,title=request.POST['title'], content=request.POST['detail'], 
    pub_date=timezone.now()) #recuritment --> 필요없다. 조회할때만 모집중인지 아닌지 버튼으로 ex 좋아요, 싫어요
    b.save()
    return HttpResponseRedirect(reverse('boardapp:home'))

def create_reply(request, postNum): # 상세 페이지에서 댓글 동록시 submit 처리
    b = Board.objects.get(postNum = postNum)
    b.reply_set.create(comment=request.POST['comment'], rep_date=timezone.now())
    return HttpResponseRedirect(reverse('boardapp:detail', args=(postNum,)))  

def main(request):
    return render(request,'boardapp/main.html')

def update(request, board_id):
    b = Board.objects.get(postNum= board_id)
    temp = Board.objects.get(postNum= board_id)
    if request.method == "POST":
        b.title=request.POST['title']
        if b.title == "":
            b.title = temp.title
        b.content=request.POST['detail']
        if b.content == "":
            b.content = temp.content
        b.pub_date=timezone.now()
        b.save()
        return HttpResponseRedirect(reverse('boardapp:detail',args=(board_id,)))
    else:
        b=Board
        return render(request, 'boardapp/update.html', {'boardapp':b})

def delete(request, board_id):
    b = Board.objects.get(postNum=board_id)
    b.delete()
    return redirect('boardapp:home')

def search(request):
    search = request.GET.get('search')
    if search=='':
        searchBoard = Board.objects.all().order_by('-postNum')[:5]
    else:
        try:
            searchBoard = Board.objects.filter(title__contains=search).order_by('-postNum')
        except:
            searchBoard = Board.objects.all().order_by('-postNum')[:5]

    return render(request, 'boardapp/home.html', {'board':searchBoard})