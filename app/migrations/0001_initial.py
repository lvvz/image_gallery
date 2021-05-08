# Generated by Django 3.2.2 on 2021-05-08 19:48

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import imagekit.models.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb', imagekit.models.fields.ProcessedImageField(upload_to='app/images_storage')),
                ('is_visible', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('element', 'is_visible'),
            },
            managers=[
                ('visible', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('text', models.TextField(max_length=1024)),
            ],
            options={
                'ordering': ('title', 'text'),
            },
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.author')),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.description')),
            ],
            options={
                'ordering': ('author', 'timestamp', 'description'),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Timestamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('modified', 'created'),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', imagekit.models.fields.ProcessedImageField(upload_to='app/images_storage')),
                ('thumb', imagekit.models.fields.ProcessedImageField(upload_to='app/images_storage')),
                ('alt', models.CharField(default=uuid.uuid4, max_length=255)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('slug', models.SlugField(default=uuid.uuid4, editable=False, max_length=70)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.album')),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.element')),
            ],
        ),
        migrations.AddField(
            model_name='element',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
        migrations.AddField(
            model_name='element',
            name='timestamp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.timestamp'),
        ),
        migrations.AddField(
            model_name='album',
            name='element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.element'),
        ),
    ]
