# Generated by Django 4.0.4 on 2022-05-18 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0007_alter_post_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1, unique=True)),
                ('post_id', models.ManyToManyField(blank=True, null=True, to='socialapp.post')),
            ],
        ),
    ]