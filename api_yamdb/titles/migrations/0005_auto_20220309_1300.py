# Generated by Django 2.2.16 on 2022-03-09 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
        ('titles', '0004_auto_20220309_1210'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Titles',
            new_name='Title',
        ),
    ]
