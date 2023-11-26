from django.urls import path,include
from inventory import views

urlpatterns = [
    path('', views.index, name='index'),
    path('a', views.add_page, name='add'),
    path('r', views.remove_page, name='remove'),
    # Diğer URL şablonlarını burada tanımlayın
]