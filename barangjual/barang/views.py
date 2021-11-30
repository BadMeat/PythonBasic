from django.shortcuts import redirect, render, redirect

from barang.models import Barang

from .forms import BarangForm

# Create your views here.

def barang_list(request):
    context = {'barang_list' : Barang.objects.all()}
    return render(request, "barang/barang_list.html", context)

def barang_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = BarangForm()
        else: 
            barang = Barang.objects.get(pk=id) 
            form = BarangForm(instance=barang)   
        return render(request, "barang/barang_form.html", {'form': form})
    else:
        if id == 0:
            form = BarangForm(request.POST)
        else: 
            barang = Barang.objects.get(pk=id) 
            form = BarangForm(request.POST,instance=barang)
        if form.is_valid():
            form.save()
        return redirect('/barang/list')
def barang_delete(request,id):
    barang = Barang.objects.get(pk=id) 
    barang.delete()
    return redirect('/barang/list')