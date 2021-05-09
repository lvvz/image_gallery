from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile


USER_CUSTOM_FIELDS = (
    'email',
    'gender',
    'birthday',
)


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + USER_CUSTOM_FIELDS


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = USER_CUSTOM_FIELDS


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location')
