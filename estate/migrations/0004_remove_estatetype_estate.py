# Generated by Django 3.2.3 on 2022-03-10 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0003_auto_20220311_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estatetype',
            name='estate',
        ),
    ]
