from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *


def page_index(request):
    return render(request, 'albuns/index.html', {})

def list_albuns(request):
    albuns = Album.objects.all()
    return render(request, 'albuns/list_albuns.html', {'albuns': albuns})

def list_musicas(request):
    musicas = Musica.objects.all()
    return render(request, 'albuns/list_musicas.html', {'musicas': musicas})

def albuns_new(request):
    return render(request, 'albuns/albuns_edit.html', {})

def musicas_new(request):
    albuns = Album.objects.all()
    return render(request, 'albuns/musicas_edit.html', {'albuns': albuns})

def albuns_add(request):
    nome_form = request.POST.get("nome")
    data_lancamento_form = request.POST.get("data_lancamento")
    banda_form = request.POST.get("banda")

    album = Album(
        nome = nome_form,
        data_lancamento = data_lancamento_form,
        banda = banda_form
    )
    album.save()
    return redirect('/albuns/')

def musicas_add(request):
    album_form = Album.objects.get(nome=request.POST.get("album"))
    print(album_form)
    nome_form = request.POST.get("nome")
    duracao_form = request.POST.get("duracao")

    musica = Musica(
        album = album_form,
        nome = nome_form,
        duracao = duracao_form
    )
    musica.save()
    return redirect('/musicas/')