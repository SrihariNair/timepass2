# Generated by Django 2.0.7 on 2018-07-04 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20180704_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userposts',
            old_name='author',
            new_name='userposts',
        ),
    ]