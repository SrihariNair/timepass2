# Generated by Django 2.0.7 on 2018-07-04 08:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_userpost_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='from_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='to_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
