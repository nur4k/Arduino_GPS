# Generated by Django 4.2.7 on 2023-11-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_item_transmitter_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='transmitter_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID передатчика'),
        ),
    ]