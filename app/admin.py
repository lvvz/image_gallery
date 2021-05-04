from django.contrib import admin
from .models import Album, Image


@admin.register(Album)
class AlbumModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class AlbumImageModelAdmin(admin.ModelAdmin):
    pass
