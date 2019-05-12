from django.contrib import admin
from .models import Album, Imagem, ImagemAlbum


class AlbumAdmin(admin.ModelAdmin):
    def save(self, request, obj, *args, **kwargs):
        if not obj.user:
            obj.user = request.user
        super(obj.user, self).save(*args, **kwargs)


admin.site.register(Album, AlbumAdmin)
admin.site.register(Imagem)
admin.site.register(ImagemAlbum)
