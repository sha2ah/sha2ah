# Generated by Django 3.2.3 on 2022-03-10 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0002_rename_type_estate_estate_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estate',
            name='estate_type',
        ),
        migrations.CreateModel(
            name='EstateType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estate.estate')),
            ],
        ),
    ]
