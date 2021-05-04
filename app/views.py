from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Album, Image


# TODO: refactor to class
def visible_albums_list(request):
    return render(request,
                  'app/album/list.html',
                  {
                      'albums': Album.visible.all()
                  }
                  )


class AlbumDetail(DetailView):
    model = Album

    def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context['images'] = Image.objects.filter(album=self.object.id)
        return context
