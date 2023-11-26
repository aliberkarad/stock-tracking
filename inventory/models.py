from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class Warehouse(models.Model):

    product = models.CharField(max_length=100, null=False, verbose_name="Ürün Adı")
    serial_number = models.CharField(max_length=100, unique=True, blank=True, verbose_name="Ürün Kodu")
    quantity = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=False, verbose_name="Adet")

    def __str__(self):
        return self.serial_number

    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'

@receiver(pre_save, sender=Warehouse)
def convert_serial_number_to_uppercase(sender, instance, **kwargs):
    instance.serial_number = instance.serial_number.upper()