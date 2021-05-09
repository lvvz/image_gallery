from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


class User(AbstractUser):
    birthday = models.DateField(null=True)
    MALE = 'M'
    FEMALE = 'F'
    gender = models.CharField(
        max_length=1,
        choices=[
            (MALE, 'Male'),
            (FEMALE, 'Female'),
        ],
    )


users = User.objects.all().select_related('profile')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
