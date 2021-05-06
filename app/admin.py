from django.contrib import admin
from .models import *


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Timestamp)
class TimestampAdmin(admin.ModelAdmin):
    pass


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
