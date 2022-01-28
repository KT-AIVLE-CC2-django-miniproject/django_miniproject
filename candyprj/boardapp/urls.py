from django.urls import path
from . import views

app_name = 'boardapp'
urlpatterns = [

    path('main/', views.main, name = 'main'),
    path('board/', views.board, name ='board'),
    path('home/', views.home, name='home'),
    path('search/', views.search),

    #스터디 모집 게시판
    path('', views.index, name='index'),
    path('<int:postNum>/', views.detail, name='detail'),
    path('write/', views.write, name='write'),
    path('write/write_board', views.write_board, name='write_board'),
    path('<int:postNum>/create_reply/', views.create_reply, name='create_reply'),
    path('<int:board_id>/update/', views.update, name ='update'),
    path('<int:board_id>/delete/', views.delete, name ='delete'),

    #공유 게시판
    path('sharedetail/<int:topicid>/', views.sharedetail, name='sharedetail'),
    # path('<int:board_id>/update1/', views.update1, name ='update1'),
    # path('<int:board_id>/delete1/', views.delete1, name ='delete1'),
    # path('<int:writter>/create1_reply/', views.create1_reply, name='create1_reply'),
    # path('<int:id>/', views.detail1, name='detail1'),
    path('new/new_write/' , views.new_write, name='new_write'), 
    
    # path('download/<id>', views.download, name = 'download'),
    # path('filedelete/<id>', views.file_delete, name ='file_delete'),
    
    path('sharedetail/<int:topicid>/', views.sharedetail, name='sharedetail'),
    path('sharedetail1/<int:postid>/', views.sharedetail1, name='sharedetail1'),
    path('main/', views.main, name = 'main'),
    path('board/', views.board, name ='board'),
    path('home/', views.home, name='home'),

    path('share/',views.share, name = 'share'),
    path('new/' , views.new_topic, name='new_topic'), #게시글 작성 페이지 url 추가 board/new/ ?
    path('replys/' , views.new_replys, name='replys'), 
]