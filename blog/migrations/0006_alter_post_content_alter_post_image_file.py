# Generated by Django 5.0.7 on 2024-07-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_content_alter_post_image_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_file',
            field=models.ImageField(upload_to='post_image_files'),
        ),
    ]
