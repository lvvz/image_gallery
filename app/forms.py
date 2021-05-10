from django import forms
from app.models import *


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = []


class TimestampForm(forms.ModelForm):
    class Meta:
        model = Timestamp
        exclude = []


class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Description
        exclude = []


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        exclude = []


class ElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ()


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('element', )

