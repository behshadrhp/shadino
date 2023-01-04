from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity']
    list_editable = ['quantity']
    list_per_page = 10
    search_fields = ['product__title__icontains']
    fields = ['cart', 'product', 'quantity']
    autocomplete_fields = ['product', 'cart']


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'created']
    list_per_page = 10
    search_fields = ['created__icontains']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title__icontains',
                     'description__icontains', 'collection__title__icontains']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Promotion)
class PromotionAdmin(admin.ModelAdmin):
    pass
