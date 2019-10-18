from django import forms
from .models import Imagem


class ImagemForm(forms.Form):
    titulo = forms.CharField(label='Título')
    descricao = forms.CharField(label='Descrição')
    imagem = forms.ImageField(label='Imagem')
    album_id = forms.CharField(label='ID do Álbum')


class ImagemModelForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ['titulo', 'descricao', 'imagem']
