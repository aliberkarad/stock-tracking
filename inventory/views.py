from django.shortcuts import redirect, render
from django.http import HttpResponse
from inventory.models import Warehouse

# Create your views here.
def index(request):
    products = Warehouse.objects.all()

    return render(request,"inventory/index.html", {
        
        "products" : products,
        
        })

def add_page(request):

    products = Warehouse.objects.all()

    if request.method == "GET":
            product_code = request.GET.get('product-code', '')
            parameter = request.GET.get('param',0)

            if parameter == '1':
                product = Warehouse.objects.get(serial_number=product_code)
                product.quantity += 1
                product.save()
                return HttpResponse("<h1 style='font-family: Arial, Helvetica, sans-serif;text-align:center;margin:50;'>ÜRÜN SAYISI EKLENDİ<br>+1</h1>")

    if request.method == 'POST':
        product_quantity = request.POST.get('quantity', 0)
        product_code = request.POST.get('product-code', '')
        
        try:
            product = Warehouse.objects.get(serial_number=product_code)
            product.quantity = product.quantity + int(product_quantity)
            product.save()
            return redirect('index')
        except Warehouse.DoesNotExist:
            pass
    
    return render(request, "inventory/add.html", {
        
        "products" : products,
        
        })


def remove_page(request):
    products = Warehouse.objects.all()

    if request.method == "GET":
            product_code = request.GET.get('product-code', '')
            parameter = request.GET.get('param',0)

            if parameter == '1':
                product = Warehouse.objects.get(serial_number=product_code)
                product.quantity = 0 if product.quantity <= 0 else product.quantity - 1                
                product.save()
                return HttpResponse("<h1 style='font-family: Arial, Helvetica, sans-serif;text-align:center;margin:50;'>ÜRÜN SAYISI ÇIKARILDI<br>-1</h1>")

    if request.method == 'POST':
        product_quantity = request.POST.get('quantity', 0)
        product_code = request.POST.get('product-code', '')
        try:
            product = Warehouse.objects.get(serial_number=product_code)
            product.quantity = product.quantity - int(product_quantity)
            if product.quantity <= 0:
                product.quantity = 0
            product.save()
            return redirect('index')
        except Warehouse.DoesNotExist:
            pass

    return render(request, "inventory/remove.html", {
        
        "products" : products,
        
        })