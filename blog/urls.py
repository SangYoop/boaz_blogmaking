#coding: utf-8

from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.index, name = 'index'),
    url(r'^write/$', views.write, name='write'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'^reply_write/$', views.reply_write, name='reply_write'),
    url(r'^reply/(?P<pk>\d+)/delete/$', views.reply_delete, name='reply_delete'),
]
##r : signal for regular formular
## pk 하나만 알려주면 되는데 post를 쓰는 것은 비효율적이라 댓글삭제는 get 사용
