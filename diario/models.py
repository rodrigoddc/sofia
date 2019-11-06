from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model


class Album(models.Model):
    JANEIRO = 'JAN'
    FEVEREIRO = 'FEV'
    MARÇO = 'MAR'
    ABRIL = 'ABR'
    MAIO = 'MAIO'
    JUNHO = 'JUN'
    JULHO = 'JUL'
    AGOSTO = 'AGO'
    SETEMBRO = 'SET'
    OUTUBRO = 'OUT'
    NOVEMBRO = 'NOV'
    DEZEMBRO = 'DEZ'

    MESES = (
        (JANEIRO, 'Janeiro'),
        (FEVEREIRO, 'Fevereiro'),
        (MARÇO, 'Março'),
        (ABRIL, 'Abril'),
        (MAIO, 'Maio'),
        (JUNHO, 'Junho'),
        (JULHO, 'Julho'),
        (AGOSTO, 'Agosto'),
        (SETEMBRO, 'Setembro'),
        (OUTUBRO, 'Outubro'),
        (NOVEMBRO, 'Novembro'),
        (DEZEMBRO, 'Dezembro'),
    )

    mes = models.CharField(choices=MESES, default=JANEIRO, max_length=3)
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=300, null=False, blank=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    verbose_name_plural = 'Álbuns'

    def save_model(self, request, obj, form, change):
        if not change:
            # the object is being created, so set the user
            obj.usuario = request.user
        obj.save()

    def __str__(self):
        return self.titulo


class Imagem(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=300, null=False, blank=False)
    imagem = models.ImageField(upload_to='imagens_album', null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    verbose_name_plural = 'Imagens'

    def __str__(self):
        return self.titulo


class Diario(models.Model):
    titulo = models.CharField(max_length=100, default='titulo')
    album = models.ForeignKey(Album, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
