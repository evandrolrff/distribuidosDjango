from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.page_index, name='page_index'),
    url(r'^albuns/$', views.list_albuns, name='list_albuns'), 
    url(r'^musicas/$', views.list_musicas, name='list_musicas'),
    url(r'^albuns/new/$', views.albuns_new, name='albuns_new'),
    url(r'^musicas/new/$', views.musicas_new, name='musicas_new'),
    url(r'^albuns_add/$', views.albuns_add, name='albuns_add'),
    url(r'^musicas_add/$', views.musicas_add, name='musicas_add'),
]