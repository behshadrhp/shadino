from django.contrib import admin
from .models import LikeItem

# Register your models here.

@admin.register(LikeItem)
class LikeItemAdmin(admin.ModelAdmin):
    pass