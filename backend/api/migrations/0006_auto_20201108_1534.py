# Generated by Django 3.1.2 on 2020-11-08 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20201108_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game_genre',
            old_name='genreName',
            new_name='genre_name',
        ),
    ]
