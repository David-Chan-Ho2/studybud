# Generated by Django 3.2.7 on 2025-01-30 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.RemoveField(
            model_name='room',
            name='host',
        ),
        migrations.RemoveField(
            model_name='room',
            name='participants',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
