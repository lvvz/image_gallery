from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import login_required
from django.shortcuts import render, redirect
from django.db import transaction
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(generic.TemplateView, LoginRequiredMixin):
    model = Profile
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        return dict(
            super(ProfileView, self).get_context_data(**kwargs),
            user=self.request.user,
            profile=self.request.user.profile,
        )


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(
        request,
        'registration/update_profile.html',
        {
            'user_form': user_form,
            'profile_form': profile_form
        }
    )
