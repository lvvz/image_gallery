from django.db import models
import imagekit.models
from imagekit.processors import ResizeToFit
import uuid


class VisibleManager(models.Manager):
    def get_queryset(self):
        return super(VisibleManager, self).get_queryset().filter(is_visible=True)


class Author(models.Model):
    name = models.CharField(max_length=70)

    class Meta:
        ordering = (
            'name',
        )


class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = (
            'modified',
            'created',
        )


class Description(models.Model):
    title = models.CharField(max_length=70)
    text = models.TextField(max_length=1024)

    class Meta:
        ordering = (
            'title',
            'text',
        )


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = (
            'name',
        )


class Element(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    timestamp = models.ForeignKey(Timestamp, on_delete=models.CASCADE)
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = (
            'author',
            'timestamp',
            'description',
        )


def image_field(size, quality):
    return imagekit.models.ProcessedImageField(
        upload_to='app/images_storage',
        processors=[ResizeToFit(size)],
        format='JPEG',
        options={
            'quality': quality
        }
    )


class Album(models.Model):
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    thumb = image_field(size=300, quality=90)
    is_visible = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = (
            'element',
            'is_visible',
        )

    visible = VisibleManager()


class Image(models.Model):
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.PROTECT)
    data = image_field(size=1280, quality=70)
    thumb = image_field(size=300, quality=80)
    alt = models.CharField(max_length=255, default=uuid.uuid4)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    slug = models.SlugField(
        max_length=70,
        default=uuid.uuid4,
        editable=False
    )
