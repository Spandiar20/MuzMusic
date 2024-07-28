# Generated by Django 5.0.7 on 2024-07-28 14:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_category_post_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='audio_file',
            field=models.FileField(null=True, upload_to='post_audio_files'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_file',
            field=models.ImageField(null=True, upload_to='post_image_files'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
