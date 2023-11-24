# Generated by Django 4.2.7 on 2023-11-24 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_item_transmitter_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='direction',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Направление'),
        ),
        migrations.AlterField(
            model_name='item',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='item',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='item',
            name='speed',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Скорость'),
        ),
    ]
