# Generated by Django 5.2.1 on 2025-06-01 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_film_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='search_field',
            field=models.CharField(blank=True, verbose_name=255),
        ),
        migrations.AddField(
            model_name='film',
            name='search_field',
            field=models.CharField(blank=True, verbose_name=255),
        ),
    ]
