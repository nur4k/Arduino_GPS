# Generated by Django 4.2.7 on 2023-11-13 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='transmitter_id',
            field=models.CharField(default=1, max_length=50, verbose_name='ID передатчика'),
            preserve_default=False,
        ),
    ]
