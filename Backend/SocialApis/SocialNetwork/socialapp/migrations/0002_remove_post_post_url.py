# Generated by Django 4.0.4 on 2022-05-06 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_url',
        ),
    ]
