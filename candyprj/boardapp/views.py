from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
<<<<<<< HEAD
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Board
# from userapp.models import User

=======
from audioop import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Board
>>>>>>> a7f35d57446575531a20e8780736e28573ac7303
# Create your views here.
def home(request):
    all_boards = Board.objects.all().order_by("-pub_date")
    paginator = Paginator(all_boards, 10)
    page = int(request.GET.get('page',1))
    board_list = paginator.get_page(page)
<<<<<<< HEAD
    return render(request, 'board/home.html', {'title': 'board List',
=======
    return render(request, 'boardapp/home.html', {'title': 'Board List',
>>>>>>> a7f35d57446575531a20e8780736e28573ac7303
    'board_list' : board_list})

def detail(request, postNum):
    board = Board.objects.get(id=postNum)
<<<<<<< HEAD
    return render(request, 'board/detail.html', {'boardapp':board})

def create(request):
    return render(request, 'board/create.html')
=======
    return render(request, 'boardapp/detail.html', {'board':board})

def create(request):
    return render(request, 'boardapp/create.html')
>>>>>>> a7f35d57446575531a20e8780736e28573ac7303

def write_board(request, postNum):
    wboard = Board(title=request.POST['title'], 
    content = request.POST['detail'], id = 'kim', pub_date=timezone.now())
    wboard.save()
<<<<<<< HEAD
    return HttpResponseRedirect(reverse('boardapp.detail', args=(postNum,)))
=======
    return HttpResponseRedirect(reverse('board:detail'))
>>>>>>> a7f35d57446575531a20e8780736e28573ac7303
