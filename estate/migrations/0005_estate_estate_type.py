# Generated by Django 3.2.3 on 2022-03-10 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0004_remove_estatetype_estate'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='estate_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='estate.estatetype'),
        ),
    ]
