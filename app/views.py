from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Album, Image


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
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context['images'] = Image.objects.filter(album=self.object.id)
        return context
