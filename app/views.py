from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Album, Image


class AlbumsList(ListView):
    model = Album
    context_object_name = 'albums'
    paginate_by = 3


# class VisibleAlbumsList(ListView):
#     queryset = Album.visible.all()
#     context_object_name = 'visible_albums'
#     paginate_by = 3
#     template_name = 'app/visible_albums_list.html'


class AlbumDetail(DetailView):
    model = Album

    def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context['images'] = Image.objects.filter(album=self.object.id)
        return context
