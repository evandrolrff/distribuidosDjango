from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *


def page_index(request):
    return render(request, 'albuns/index.html', {})

def list_albuns(request):
    albuns = Albuns.objects.all()
    context = {
        'albuns' : albuns,
    }
    return render(request, 'albuns/list_albuns.html', context)

def list_musicas(request):
    musicas = Musica.objects.all()
    context = {
        'musicas': musicas,
    }

    return render(request, 'albuns/list_musicas.html', context)
