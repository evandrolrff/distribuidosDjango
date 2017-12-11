from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *
from .forms import *
from .utils import *


def page_index(request):    
    return render(request, 'albuns/index.html', {})

def list_albuns(request):
    albuns = Album.objects.all()
    images = [(util(album.nome, album.banda), album) for album in albuns]
    context = {         
        'images': images,
    }
    return render(request, 'albuns/list_albuns.html', context)

def list_musicas(request):
    musicas = Musica.objects.all()
    images = [()]
    for musica in musicas:
        album = Album.objects.get(nome=musica.album)
        images += [(util(musica.album, album.banda), musica)]
    
    images.pop(0)
    print(images)
    context = {
        'images': images,
    }
    return render(request, 'albuns/list_musicas.html', context)

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

def musicas_delete(request, pk, template_name='musicas_delete.html'):
    musica = get_object_or_404(Musica, pk=pk)
    musica.delete()
    return redirect('list_musicas')

def albuns_delete(request, pk, template_name='albuns_delete.html'):
    album = get_object_or_404(Album, pk=pk)
    musicas = Musica.objects.filter(album=pk)
    for musica in musicas:
        musica.delete()
    album.delete()
    return redirect('list_albuns')

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
