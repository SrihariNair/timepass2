# Generated by Django 2.0.7 on 2018-07-04 07:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20180704_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
