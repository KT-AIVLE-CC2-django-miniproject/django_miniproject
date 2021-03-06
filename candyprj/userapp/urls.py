from django.urls import path
from . import views


app_name = 'userapp'
urlpatterns = [
     path('signup/', views.signup, name='signup'),
     path('profile/', views.profile, name='profile'),
     path('update/', views.update, name='update'),
     path('login/', views.login, name='login'),
     path('logout/', views.logout, name='logout'),
     path('<str:id>/', views.userinfo, name='userinfo'),
     # path('img_show/', views.img_show, name='img_show'),
]