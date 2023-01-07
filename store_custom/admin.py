from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin
from tag.models import TagItem
from store.models import Product

# Register your models here.


class TagInLine(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TagItem


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInLine]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)