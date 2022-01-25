from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Board
# from userapp.models import User

# Create your views here.
def home(request):
    all_boards = Board.objects.all().order_by("-pub_date")
    paginator = Paginator(all_boards, 10)
    page = int(request.GET.get('page',1))
    board_list = paginator.get_page(page)
    return render(request, 'board/home.html', {'title': 'board List',
    'board_list' : board_list})

def detail(request, postNum):
    board = Board.objects.get(id=postNum)
    return render(request, 'board/detail.html', {'boardapp':board})

def create(request):
    return render(request, 'board/create.html')

def write_board(request, postNum):
    wboard = Board(title=request.POST['title'], 
    content = request.POST['detail'], id = 'kim', pub_date=timezone.now())
    wboard.save()
    return HttpResponseRedirect(reverse('boardapp.detail', args=(postNum,)))
