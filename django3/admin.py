# subscribe/admin.py
from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')  # Kolom yang ditampilkan di daftar admin
    search_fields = ('first_name', 'last_name', 'email')  # Opsi pencarian

admin.site.register(Customer, CustomerAdmin)
