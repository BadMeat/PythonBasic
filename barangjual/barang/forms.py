from django import forms
from django.forms import fields
from .models import Barang

class BarangForm(forms.ModelForm):
    class Meta: 
        model = Barang
        fields = '__all__'
        # fields = ('namabarang','keterangan')
        labels = {
            'namabarang' : 'Nama Barang',
            'position' : 'Jenis'
        }

    def __init__(self, *args, **kwargs):
        super(BarangForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "--Pilih---"
        self.fields['keterangan'].required = False