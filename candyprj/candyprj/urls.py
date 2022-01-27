from http.client import ImproperConnectionState
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

#신규작성
# from boardapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('boardapp.urls')),
    path('user/', include('userapp.urls')),


    # path('board/new/' , views.new_topic, name='new_topoc'), #게시글 작성 페이지 url 추가 board/new/ ?
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

