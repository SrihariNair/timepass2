# Generated by Django 2.0.6 on 2018-06-30 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_customuser_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='resume',
            field=models.FileField(upload_to=''),
        ),
    ]