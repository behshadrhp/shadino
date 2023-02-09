from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from . import views

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet, basename='collection')
router.register('carts', views.CartItemViewSet, basename='cart')
router.register('customers', views.CustomerView, basename='customer')

product_router = NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet,
                        basename='product-reviews')

cart_item = NestedDefaultRouter(router, 'carts', lookup='cart')
cart_item.register('items', views.CartViewSet, basename='cart-item')

urlpatterns = router.urls + product_router.urls + cart_item.urls
