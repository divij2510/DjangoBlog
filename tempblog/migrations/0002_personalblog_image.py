# Generated by Django 4.2.5 on 2023-10-05 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalblog',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
