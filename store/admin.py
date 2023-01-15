from django.contrib import admin
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
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
    list_display = ['title', 'price', 'collection', 'created', 'updated']
    list_per_page = 10
    list_filter = ['collection']
    search_fields = ['title__icontains', 'description__icontains']
    autocomplete_fields = ['collection', 'promotion']
    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'payment_status', 'placed_at']
    list_per_page = 10
    list_filter = ['payment_status']
    search_fields = ['customer__first_name__icontains',
                     'customer__last_name__icontains']
    fields = ['payment_status', 'customer']
    autocomplete_fields = ['customer']


@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity',
                    'price', 'final_price', 'created']
    list_per_page = 10
    search_fields = ['order__customer__first_name__icontains',
                     'order__customer__last_name__icontains', 'product__title__icontains']
    fields = ['order', 'product', 'quantity']
    autocomplete_fields = ['order', 'product']

    @admin.display(description='قیمت واحد')
    def price(self, product: models.OrderItem):
        return product.product.price

    @admin.display(description='قیمت نهایی')
    def final_price(self, product: models.OrderItem):
        return product.quantity * product.product.price


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count', 'featured_product', 'created']
    list_per_page = 10
    search_fields = ['title__icontains']
    fields = ['title', 'featured_product']
    autocomplete_fields = ['featured_product']

    @admin.display(description='محصولات این مجموعه')
    def product_count(self, collection: models.Collection):
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'collection__id': str(collection.id)
            })
        )
        return format_html(f'<a href="{url}">{collection.product_count}</a>')

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count=Count('collection_item')
        )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email',
                    'phone', 'membership', 'birthday', 'created']
    list_filter = ['membership']
    list_per_page = 10
    search_fields = ['first_name__icontains',
                     'last_name__icontains', 'email__icontains', 'phone__icontains']
    fields = ['first_name', 'last_name', 'email',
              'phone', 'birthday', 'membership']


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'city', 'street', 'created']
    list_filter = ['city']
    list_per_page = 10
    fields = ['customer', 'city', 'street']
    autocomplete_fields = ['customer']


@admin.register(models.Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['description', 'discount', 'created']
    list_per_page = 10
    search_fields = ['description__icontains']
    fields = ['description', 'discount']
