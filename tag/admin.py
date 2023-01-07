from django.contrib import admin
from .models import Tag, TagItem

# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['label']


@admin.register(TagItem)
class TagItemAdmin(admin.ModelAdmin):
    search_fields = ['tag__label__icontains']
