from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from . import views

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet, basename='collections')
router.register('carts', views.CartItemViewSet, basename='carts')
router.register('customers', views.CustomerViewSet, basename='customers')
router.register('orders', views.OrderViewSet, basename='orders')

product_router = NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet,
                        basename='product-reviews')
product_router.register(
    'images', views.ProductImageViewSet, basename='product-images')

cart_item = NestedDefaultRouter(router, 'carts', lookup='cart')
cart_item.register('items', views.CartViewSet, basename='cart-item')

urlpatterns = router.urls + product_router.urls + cart_item.urls
