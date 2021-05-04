#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import uuid
from django.db import models
import imagekit.models
from imagekit.processors import ResizeToFit


class VisibleManager(models.Manager):
    def get_queryset(self):
        return super(VisibleManager,self).get_queryset().filter(is_visible=True)


class Album(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=1024)
    thumb = imagekit.models.ProcessedImageField(
        upload_to='albums',
        processors=[ResizeToFit(300)],
        format='JPEG',
        options={
            'quality': 90
        }
    )
    tags = models.CharField(max_length=250)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)

    visible = VisibleManager()

    def __unicode__(self):
        return self.title


class Image(models.Model):
    image = imagekit.models.ProcessedImageField(
        upload_to='albums',
        processors=[ResizeToFit(1280)],
        format='JPEG',
        options={
            'quality': 70
        }
    )
    thumb = imagekit.models.ProcessedImageField(
        upload_to='albums',
        processors=[ResizeToFit(300)],
        format='JPEG',
        options={
            'quality': 80
        }
    )
    album = models.ForeignKey('album', on_delete=models.PROTECT)
    alt = models.CharField(max_length=255, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    slug = models.SlugField(
        max_length=70,
        default=uuid.uuid4,
        editable=False
    )
