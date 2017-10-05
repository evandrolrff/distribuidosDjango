from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *


def page_index(request):
    return render(request, 'albuns/index.html', {})

def list_albuns(request):
    return render(request, 'albuns/list_albuns.html', {})

def list_musicas(request):
    return render(request, 'albuns/list_musicas.html', {})