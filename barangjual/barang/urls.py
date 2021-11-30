from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.barang_form, name='barang_insert'),
    path('<int:id>/', views.barang_form, name="barang_update"),
    path('list/',views.barang_list, name='barang_list'),
    path('delete/<int:id>/',views.barang_delete, name='barang_delete')
]
