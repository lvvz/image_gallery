import django.views.generic
from django.views.generic import DetailView, ListView, FormView, View, TemplateView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *

from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import login_required
from django.shortcuts import render, redirect

from rest_framework import serializers
# , generics, viewsets, views


class AlbumsList(ListView, LoginRequiredMixin):
    model = Album
    context_object_name = 'albums'
    paginate_by = 3


@login_required
def create_album(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST, instance=Author())
        timestamp_form = TimestampForm(request.POST, instance=Timestamp())
        description_form = DescriptionForm(request.POST, instance=Description())
        element_form = ElementForm(request.POST, instance=Element())
        album_form = AlbumForm(request.POST, request.FILES, instance=Album())
        if all(form.is_valid() for form in [author_form, timestamp_form, description_form, element_form, album_form]):
            new_author = author_form.save()
            new_timestamp = timestamp_form.save()
            new_description = description_form.save()
            new_element = element_form.save(commit=False)
            new_element.author = new_author
            new_element.timestamp = new_timestamp
            new_element.description = new_description
            new_element.save()
            new_album = album_form.save(commit=False)
            new_album.element = new_element
            new_album.save()
            messages.success(request, _('Create was successful!'))
            return redirect('album_list')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        author_form = AuthorForm(instance=Author())
        timestamp_form = TimestampForm(instance=Timestamp())
        description_form = DescriptionForm(instance=Description())
        element_form = ElementForm(instance=Element())
        album_form = AlbumForm(instance=Album())
    return render(
        request,
        'app/album_form.html',
        {
            'author': author_form,
            'timestamp': timestamp_form,
            'description': description_form,
            'element': element_form,
            'album': album_form,
        }
    )


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


class AboutView(TemplateView):
    template_name = 'app/about.html'

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            about_info_strings=[
                "This is image gallery",
                "Made by O. Vovchok.",
            ]
        )


# class AlbumListAPIView(viewsets.ModelViewSet):
#     queryset = Album.objects.all()
#     serializer_class = AlbumSerializer
