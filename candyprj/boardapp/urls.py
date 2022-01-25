from django.urls import path
from . import views

app_name = 'boardapp'
urlpatterns = [
<<<<<<< HEAD
    path('home', views.home, name ='home'),
    # path('<int:board_id>/', views.detail, name ='detail'),
    # path('create/', views.create, name ='create'),
    # path('create/write_board', views.write_board, name ='write_board'),
    #path('<int:board_id>/create_reply', views.creat_reply, name ='create_reply'),
=======
    path('', views.home, name ='home'),
    path('<int:board_id>/', views.detail, name ='detail'),
    path('create/', views.create, name ='create'),
    path('create/write_board', views.write_board, name ='write_board'),
    # #path('<int:board_id>/create_reply', views.creat_reply, name ='create_reply'),
>>>>>>> 5fd50adc93431fdfed6d4b4097c06388bc37ee08
]