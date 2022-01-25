from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from matplotlib.pyplot import title
from .models import Board
from userapp.models import User
# from userapp.models import User

# Create your views here.
def home(request):
    all_boards = Board.objects.all().order_by("-pub_date")
    paginator = Paginator(all_boards, 10)
    page = int(request.GET.get('page',1))
    board_list = paginator.get_page(page)
    return render(request, 'boardapp/home.html', {'title': 'Board List',
    'board_list' : board_list})

def detail(request, postNum):
    board = Board.objects.get(id=postNum)
    return render(request, 'boardapp/detail.html', {'boardapp':board})

def create(request):
    return render(request, 'boardapp/create.html')

def write_board(request):
    u = User.objects.get(id='kjh')
    wboard = Board(id= u, title=request.POST['title'], 
    content = request.POST['detail'], pub_date=timezone.now())
    wboard.save()
    # return HttpResponseRedirect(reverse('boardapp.detail', args=(postNum,)))


def post(request):
    if request.method =="POST":
        title = request.POST['title']
        content = request.POST['content']
        # id = request.POST['id']
        board = Board(title = title, content = content)
        board.save()
        # return redirect(home)
        return HttpResponseRedirect(reverse('boardapp.home'))
    else:
        return render(request,'boardapp/post.html')

# def detail1(request, id): id받아와서 게시글 보기



