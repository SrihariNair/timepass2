# Generated by Django 2.0.7 on 2018-07-06 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_userposts_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userposts',
            name='author',
        ),
    ]