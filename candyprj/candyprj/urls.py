from django.contrib import admin
from django.urls import path, include

#신규작성
# from boardapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('boardapp.urls')),
    path('user/', include('userapp.urls')),

    # path('board/new/' , views.new_topic, name='new_topoc'), #게시글 작성 페이지 url 추가 board/new/ ?
]
