# Generated by Django 4.2 on 2023-04-26 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='decription',
            new_name='description',
        ),
    ]