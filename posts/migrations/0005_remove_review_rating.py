# Generated by Django 4.2 on 2023-04-26 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
    ]
