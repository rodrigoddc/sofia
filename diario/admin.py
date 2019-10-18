from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Album, Imagem


class ImagemInline(admin.TabularInline):
    model = Imagem
    extra = 1


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Álbum',
         {'fields': ['mes', 'titulo', 'descricao']}),
    ]
    list_filter = ('titulo', 'mes')
    inlines = [ImagemInline]

    def save_model(self, request, obj, form, change):
        if not change:
            # the object is being created, so set the user
            obj.usuario = request.user
        obj.save()


admin.site.register(Album, AlbumAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)

# default: "Django Administration"
admin.site.site_header = 'Diário do bebê'
# default: "Site administration"
admin.site.index_title = 'Alterações'
# default: "Django site admin"
admin.site.site_title = 'Administração'