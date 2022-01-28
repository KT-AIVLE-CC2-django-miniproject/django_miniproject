from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.urls import reverse
from django.core.paginator import Paginator
from matplotlib.pyplot import title
from userapp.models import User

from .models import Board, Topic, Replys

# from userapp.views import ss

#기본페이지
# def index(request):
#     return render(request, 'boardapp/index.html', {'title':'data'})

def home(request):
    # all_boards = Board.objects.order_by('-pub_date')
    kw = request.GET.get('kw', '')  # 검색어
    all_boards = Board.objects.filter(title__contains=kw).order_by('-postNum')
    paginator = Paginator(all_boards, 10)
    page = request.GET.get('page','1')
    board_list = paginator.get_page(page)
    context={'all_boards':board_list}


    return render(request, 'boardapp/home.html', {'board': board_list, 'kw':kw})



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


    b = Board(id = uid,title=request.POST['title'], content=request.POST['detail'], 
    pub_date=timezone.now()) #recuritment --> 필요없다. 조회할때만 모집중인지 아닌지 버튼으로 ex 좋아요, 싫어요
    if b.title != "": #제목이 입력된 경우에만 저장
        b.save()

    return HttpResponseRedirect(reverse('boardapp:home'))

def create_reply(request, postNum): # 상세 페이지에서 댓글 동록시 submit 처리
    uid = request.session['id']
    uid = User.objects.get(id=uid)

    b = Board.objects.get(postNum = postNum)
    b.reply_set.create(id = uid, comment=request.POST['comment'], rep_date=timezone.now())
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



######################################################################기업별 면접공유 함수
from .models import Topic, Replys
from django.http import HttpResponse

def share(request):
    topics = Topic.objects.all()
    return render(request,'boardapp/share.html',{'topics':topics})
    #share html을 렌더링하고 topics 개체 반환

def sharedetail(request, topicid):
    uid = request.session['id']
    uid = User.objects.get(id = uid)
    topics = get_object_or_404(Topic, pk=topicid)
    try:
        uid = request.session['id']
        session = User.objects.get(id = uid)
        context = {
            'topics' : topics,
            'session' : session,
        }
        return render(request, 'boardapp/sharedetail.html', context)
    except KeyError:
        return redirect('boardapp:share')
    
def new_write(request): #게시글 목록에서 글쓰기 버튼 클릭 시 쓰기 페이지로 이동
    uid = request.session['id']
    uid = User.objects.get(id = uid)


    # b = Board(id = uid,title=request.POST['title'], content=request.POST['detail'], 
    topics = Topic(writter = uid, subject =request.POST['subject'], message =request.POST['message'], file = request.FILES.get('file')) 
    if topics.subject !="":
        topics.save()

def sharedetail1(request, postid):
    uid = request.session['id']
    uid = User.objects.get(id = uid)
    posts = get_object_or_404(Replys, pk=postid)
    try:
        uid = request.session['id']
        session = User.objects.get(id = uid)
        context = {
            'posts' : posts,
            'session' : session,
        }
        return render(request, 'boardapp/sharedetail1.html', context)
    except KeyError:
        return redirect('boardapp:sharedetail')

    return HttpResponseRedirect(reverse('boardapp:share'))
def new_topic(request):
    # topics = Topic.objects.all()
    # if request.method == 'POST':      
    #     uid = request.session['id']
    #     uid = User.objects.get(id = uid)
        
        # topics = Topic.objects.create(
        #     subject=subject,
        #     message=message,
        #     writter=user
        #     )
        # topics = Topic(writter = uid, subject =request.POST['subject'], message =request.POST['message'], file = request.FILES['file']) 
        # if topics.subject !="":
        #     topics.save()

        # posts = Replys.objects.create(
        #     created_at = timezone.now(),
        #     message = message,
        #     created_by=uid,
        #     updated_by=uid,
        #     updated_at = timezone.now())

    
    return render(request, 'boardapp/new_topic.html')

def new_replys(request):
    posts = Replys.objects.all()
    if request.method == 'POST':
        message = request.POST['message']

        uid = request.session['id']
        uid = User.objects.get(id = uid)

        posts = Replys(created_by = uid, message =request.POST['message'],created_at = timezone.now(),updated_by=uid,
        updated_at = timezone.now()) 
        posts.save()
        # posts = Replys.objects.create(
        #     created_at = timezone.now(),
        #     message = message,
        #     created_by=uid,
        #     updated_by=uid,
        #     updated_at = timezone.now())

        return redirect('boardapp:sharedetail')
    
    return render(request,'boardapp/new_replys.html',{'posts': posts})


# def replys(request, postsid):
#     uid = request.session['id']
#     uid = User.objects.get(id = uid)
#     posts = get_object_or_404(Replys, pk=postsid)
#     try:
#         uid = request.session['id']
#         session = User.objects.get(id = uid)
#         context = {
#             'posts' : posts,
#             'session' : session,
#         }
#         return render(request, 'boardapp/replys.html', context)
#     except KeyError:
#         return redirect('boardapp:share')




# def detail1(request, id): #게시글 제목 선택시 상세 페이지로 이동
#     board1 = Topic.objects.get(id=id)
#     return render(request, 'boardapp/detail1.html', {'boardapp1': board1})

# # def detail(request, postNum): #게시글 제목 선택시 상세 페이지로 이동
# #     board = Board.objects.get(postNum=postNum)
# #     return render(request, 'boardapp/detail.html', {'boardapp': board})    

# def create1_reply(request, id): # 상세 페이지에서 댓글 동록시 submit 처리
#     uid = request.session['id']
#     uid = User.objects.get(id=uid)

#     b = Topic.objects.get(id = id)
#     b.reply1_set.create(writter = uid, message=request.POST['message'], last_updated=timezone.now())
#     return HttpResponseRedirect(reverse('boardapp:detail1', args=(id,)))  

# # def create_reply(request, postNum): # 상세 페이지에서 댓글 동록시 submit 처리
# #     uid = request.session['id']
# #     uid = User.objects.get(id=uid)

# #     b = Board.objects.get(postNum = postNum)
# #     b.reply_set.create(id = uid, comment=request.POST['comment'], rep_date=timezone.now())
# #     return HttpResponseRedirect(reverse('boardapp:detail', args=(postNum,)))  


# def update1(request, board_id1):
#     b = Topic.objects.get(id= board_id1)
#     temp = Topic.objects.get(id= board_id1)
#     if request.method == "POST":
#         b.subject=request.POST['subject']
#         if b.subject == "":
#             b.subject = temp.subject
#         b.message=request.POST['message']
#         if b.message == "":
#             b.message = temp.message
#         b.last_updated=timezone.now()
#         b.save()
#         return HttpResponseRedirect(reverse('boardapp:detail1',args=(board_id1,)))
#     else:
#         b=Topic
#         return render(request, 'boardapp/update1.html', {'boardapp1':b})

# # def update(request, board_id):
# #     b = Board.objects.get(postNum= board_id)
# #     temp = Board.objects.get(postNum= board_id)
# #     if request.method == "POST":
# #         b.title=request.POST['title']
# #         if b.title == "":
# #             b.title = temp.title
# #         b.content=request.POST['detail']
# #         if b.content == "":
# #             b.content = temp.content
# #         b.pub_date=timezone.now()
# #         b.save()
# #         return HttpResponseRedirect(reverse('boardapp:detail',args=(board_id,)))
# #     else:
# #         b=Board
# #         return render(request, 'boardapp/update.html', {'boardapp':b})


# def delete1(request, board_id1):
#     b = Topic.objects.get(id=board_id1)
#     b.delete()
#     return redirect('boardapp:share')

# # def delete(request, board_id):
# #     b = Board.objects.get(postNum=board_id)
# #     b.delete()
# #     return redirect('boardapp:home')


