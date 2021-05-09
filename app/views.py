from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Album, Image

from rest_framework import serializers, generics, viewsets, views


class AlbumsList(ListView, LoginRequiredMixin):
    model = Album
    context_object_name = 'albums'
    paginate_by = 3


# class VisibleAlbumsList(ListView):
#     queryset = Album.visible.all()
#     context_object_name = 'visible_albums'
#     paginate_by = 3
#     template_name = 'app/visible_albums_list.html'


class AlbumDetail(DetailView, LoginRequiredMixin):
    model = Album

    def get_context_data(self, **kwargs):
        return dict(
            super(AlbumDetail, self).get_context_data(**kwargs),
            images=Image.objects.filter(album=self.object.id)
        )


class AlbumSerializer(serializers.ModelSerializer):
    many = True

    class Meta:
        model = Album


# class AlbumListAPIView(viewsets.ModelViewSet):
#     queryset = Album.objects.all()
#     serializer_class = AlbumSerializer
