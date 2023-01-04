from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass


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
