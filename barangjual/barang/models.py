from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Barang(models.Model):
    namabarang = models.CharField(max_length=100)
    harga = models.CharField(max_length=100)
    jumlah = models.IntegerField(default=0)
    keterangan = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)