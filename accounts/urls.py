from django.urls import path

from .views import SignUpView, ProfileView, update_profile


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('update_profile/', update_profile, name='update_profile')
]
