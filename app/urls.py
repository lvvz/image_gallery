"""image_gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from app.views import *
from django.conf.urls.static import static
from django.urls import include

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

urlpatterns = [
    path('', AlbumsList.as_view(), name='album_list'),
    path('upload', create_album, name='album_upload'),
    path('about/', AboutView.as_view(), name='about'),
    url(r'^(?P<slug>[-\w]+)$', AlbumDetail.as_view(), name='album'),
] + static('images_storage', document_root=BASE_DIR / 'app/images_storage')
