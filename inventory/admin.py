from django.contrib import admin
from inventory.models import Warehouse

# Register your models here.
@admin.register(Warehouse)
class WarehouesAdmin(admin.ModelAdmin):
    list_display = ('product', 'serial_number', 'quantity',)
    list_editable = ('quantity',)
    ordering = ('id',)