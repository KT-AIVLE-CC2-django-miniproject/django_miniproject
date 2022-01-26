from django.urls import path
from . import views

app_name = 'boardapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:postNum>/', views.detail, name='detail'),
    path('write/', views.write, name='write'),
    path('write/write_board', views.write_board, name='write_board'),
    path('<int:postNum>/create_reply', views.create_reply, name='create_reply'),
    
    path('main/', views.main, name = 'main'),
    path('board/', views.board, name ='board'),
    path('home/', views.home, name='home'),
]