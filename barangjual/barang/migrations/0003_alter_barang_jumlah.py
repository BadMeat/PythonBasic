# Generated by Django 3.2.9 on 2021-11-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0002_barang_jumlah'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='jumlah',
            field=models.IntegerField(default=0),
        ),
    ]
