# Generated by Django 4.2 on 2023-05-22 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0008_blogpostmodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]
