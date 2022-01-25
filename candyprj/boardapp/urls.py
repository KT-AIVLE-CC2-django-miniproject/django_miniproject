from django.urls import path
from . import views

app_name = 'boardapp'
urlpatterns = [
    path('home/', views.home, name ='home'),
    path('post/', views.post, name ='post'),
    path('post/reply/', views.reply, name ='reply'),
    path('<int:Board.postNum>/', views.detail, name ='detail'),
    # path('<int:board.postNum>/create_reply', views.create_reply, name ='create_reply'),
]
