from django.contrib import admin
from .models import Tag, TagItem

# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(TagItem)
class TagItemAdmin(admin.ModelAdmin):
    pass
