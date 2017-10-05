from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.page_index, name='page_index'),
    url(r'^albuns/$', views.list_albuns, name='list_albuns'), 
    url(r'^musicas/$', views.list_musicas, name='list_musicas'),
]