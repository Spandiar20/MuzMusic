# Generated by Django 5.0.7 on 2024-08-02 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_date_comment_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default='default_profile.png', upload_to='post_image_files'),
        ),
    ]
