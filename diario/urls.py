from django.urls import path, include
from .views import ListAlbuns, AlbumDetail
from home import urls as home_urls

app_name = 'diario'
urlpatterns = [
    path('', include(home_urls)),
    path('lista-albuns', ListAlbuns.as_view(), name="lista-albuns"),
    path('detail/<int:pk>', AlbumDetail.as_view(), name="album_detail"),
]