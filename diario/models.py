from django.db import models


class Imagem(models.Model):
    titulo = models.CharField(max_length=100, default='titulo')
    descricao = models.CharField(max_length=300, default='descricao')
    imagem = models.ImageField(upload_to='imagens_album', null=True, blank=True)

    def __str__(self):
        return self.titulo


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
    titulo = models.CharField(max_length=100, default='titulo')
    descricao = models.CharField(max_length=300, default='descricao')

    def __str__(self):
        return self.titulo


class ImagemAlbum(models.Model):
    imagens = models.ForeignKey(Imagem, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


class Diario(models.Model):
    album = models.ForeignKey(Album, null=True, related_name='+', on_delete=models.CASCADE)

    pass