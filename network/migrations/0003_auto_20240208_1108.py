# Generated by Django 3.0.14 on 2024-02-08 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_follow_likes_posts_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Likes',
            new_name='Like',
        ),
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]
