from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Album
from .forms import ImagemForm, ImagemModelForm


class ListAlbuns(ListView):

    def get(self, request):

        albuns = Album.objects.all()
        return render(request, 'diario/lista-albuns.html', {'albuns': albuns})

    def post(self, request):

        data = {
            'form_item': ImagemForm(),
            'titulo': request.POST['titulo'],
            'descricao': request.POST['descricao'],
            'imagem': request.POST['imagem'],
            'album_id': request.POST['album_id']}

        if data['album_id']:
            album = Album.objects.get(id=data['album_id'])
            data['titulo'] = request.POST['titulo']
            data['descricao'] = request.POST['descricao']
            data['imagem'] = request.POST['imagem']
            album.save()
        else:
            album = Album.objects.create(
                titulo=data['titulo'],
                descricao=data['descricao'],
                imagem=data['imagem'],)

        imagens = album.imagem_set.all()
        data['album'] = album
        data['itens'] = imagens

        return render(request, 'diario/album-detail.html', data)


class AlbumDetail(LoginRequiredMixin, DetailView):
    model = Album

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['albuns'] = Album.objects.get(id=context['album'].id)

        context['imagens'] = context['album'].imagem_set.all()

        return context
