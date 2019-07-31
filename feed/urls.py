from django.conf.urls import url
from . import views

app_name = 'feed'
urlpatterns = [
    url(r'^$', views.user_list, name='user_list'),
    url(r'user_list_date', views.user_list_date, name='user_list_date'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/file/$', views.post_file, name='post_file'),
]
