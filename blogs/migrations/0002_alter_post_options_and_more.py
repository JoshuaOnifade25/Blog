# Generated by Django 4.2.1 on 2023-05-25 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveIndex(
            model_name='post',
            name='blogs_post_publish_693c21_idx',
        ),
    ]
