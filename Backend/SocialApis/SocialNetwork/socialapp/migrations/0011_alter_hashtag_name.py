# Generated by Django 4.0.4 on 2022-05-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0010_remove_hashtag_post_id_hashtag_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]