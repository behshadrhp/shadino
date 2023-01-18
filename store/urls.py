from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collection', views.CollectionViewSet, basename='collection')

urlpatterns = router.urls