# Generated by Django 4.0.6 on 2022-08-23 08:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='fav_room', to=settings.AUTH_USER_MODEL),
        ),
    ]
