from django.urls import path
from . import views

app_name = 'boardapp'
urlpatterns = [
    path('home', views.home, name ='home'),
    path('post', views.post, name ='post'),
    # path('<int:board_id>/', views.detail, name ='detail'),
    # path('create/', views.create, name ='create'),
    # path('create/write_board', views.write_board, name ='write_board'),
    #path('<int:board_id>/create_reply', views.creat_reply, name ='create_reply'),
]