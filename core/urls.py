from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('store/', include('store.urls')),
]


admin.site.site_header = 'شادینو'
admin.site.site_title = 'پنل مدیریتی فروشگاه شادینو'
admin.site.index = 'فروشگاه شادینو'
