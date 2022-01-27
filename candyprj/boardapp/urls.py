from django.urls import path
from . import views

app_name = 'boardapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:postNum>/', views.detail, name='detail'),
    path('write/', views.write, name='write'),
    path('write/write_board', views.write_board, name='write_board'),
    path('<int:postNum>/create_reply/', views.create_reply, name='create_reply'),
    path('<int:board_id>/update/', views.update, name ='update'),
    path('<int:board_id>/delete/', views.delete, name ='delete'),
    
    path('main/', views.main, name = 'main'),
    path('board/', views.board, name ='board'),
    path('home/', views.home, name='home'),
    path('search/', views.search),

    path('share/',views.share, name = 'share'),
    path('new/' , views.new_topic, name='new_topoc'), #게시글 작성 페이지 url 추가 board/new/ ?
]