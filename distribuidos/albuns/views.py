from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *
from .forms import *


def page_index(request):
    return render(request, 'albuns/index.html', {})

def list_albuns(request):
    albuns = Album.objects.all()
    return render(request, 'albuns/list_albuns.html', {'albuns': albuns})

def list_musicas(request):
    musicas = Musica.objects.all()
    return render(request, 'albuns/list_musicas.html', {'musicas': musicas})

def albuns_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('/albuns/')
    else:
        form = AlbumForm()
    return render(request, 'albuns/albuns_edit.html', {'form': form})

def musicas_new(request):
    if request.method == "POST":
        form = MusicaForm(request.POST)
        if form.is_valid():
            musica = form.save(commit=False)
            musica.save()
            return redirect('/musicas/')
    else:
        form = MusicaForm()
    return render(request, 'albuns/musicas_edit.html', {'form': form})

def albuns_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('/albuns/')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albuns/albuns_edit.html', {'form': form})

def musicas_edit(request, pk):
    musica = get_object_or_404(Musica, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=musica)
        if form.is_valid():
            musica = form.save(commit=False)
            musica.save()
            return redirect('/musicas/')
    else:
        form = MusicaForm(instance=musica)
    return render(request, 'albuns/musicas_edit.html', {'form': form})

#nao utilizado
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

#nao utilizado
def musicas_add(request):
    album_form = Album.objects.get(nome=request.POST.get("album"))
    nome_form = request.POST.get("nome")
    duracao_form = request.POST.get("duracao")

    musica = Musica(
        album = album_form,
        nome = nome_form,
        duracao = duracao_form
    )
    musica.save()
    return redirect('/musicas/')

#def musicas_edit(request):
 #   pass'''