from django.contrib import admin
from .models import Category, MenuItem, Cart, Order, OrderItem

# Enregistrer les modèles dans l'interface d'administration
admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)