from django import forms
from .models import *

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('nome', 'data_lancamento', 'banda')

class MusicaForm(forms.ModelForm):

    class Meta:
        model = Musica
        fields = ('album', 'nome', 'duracao')