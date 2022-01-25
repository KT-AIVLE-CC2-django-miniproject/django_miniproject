from audioop import reverse
from django.http import HttpResponseRedirect, Http404
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

def post(request):
    if request.method =="POST":
        title = request.POST['title']
        content = request.POST['content']
        id = request.POST['id']  # 로그인 후에 세션에 저장된 값으로 id 알아내기 

        board = Board(title = title, content = content, id = id, recuritment = True)

        board.save()
        return redirect(home)
        # return HttpResponseRedirect(reverse('boardapp.home'))
    else:
        return render(request,'boardapp/post.html')

def detail(request):
    try:
        board = Board.objects.get(pk=Board.postNum) 
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'boardapp/detail.html', {'boardapp':board})

def reply(request, postNum):
    bd = Board.objects.get(id=postNum)
    bd.reply_set.create(comment=request.POST['comment'], rep_date=timezone.now())
    return HttpResponseRedirect(reverse('boardapp.detail'))

