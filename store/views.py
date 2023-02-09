from django.shortcuts import get_object_or_404
from django.db.models import ProtectedError
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .filterset import ProductFilterSet, ReviewFilterSet
from .paginations import DefaultPagination
from .models import Product, Collection, Review, CartItem, Cart, Customer
from .viewsets import CreateRetrieveDestroyGenericViewSet
from .serializers import (
    ProductSerializer,
    ProductCreateUpdateSerializer,
    CollectionSerializer,
    CollectionCreateUpdateSerializer,
    ReviewSerializer,
    CartItemSerializer,
    CartReviewItemSerializer,
    AddCartSerializer,
    UpdateCartSerializer,
    CustomerSerializer,
)


# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('-updated')
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilterSet
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'updated']
    pagination_class = DefaultPagination

    def destroy(self, request, pk):
        queryset = get_object_or_404(Product, pk=pk)
        try:
            queryset.delete()
            return Response({'پیام': 'محصول حذف شد'}, status=status.HTTP_200_OK)
        except ProtectedError:
            return Response({'پیام': 'این محصول را نمی توان حذف کرد زیرا به یک سبد خرید مرتبط است'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProductCreateUpdateSerializer
        return self.serializer_class


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all().order_by('-created')
    serializer_class = CollectionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['created']
    pagination_class = DefaultPagination

    def destroy(self, request, pk):
        queryset = get_object_or_404(Collection, pk=pk)
        try:
            queryset.delete()
            return Response({'پیام': 'این مجموعه با موفقیت حذف شد'}, status=status.HTTP_200_OK)
        except ProtectedError:
            return Response({'پیام': 'این مجموعه را نمی توان حذف کرد زیرا به یک محصول مرتبط است'}, status=status.HTTP_404_NOT_FOUND)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CollectionCreateUpdateSerializer
        return self.serializer_class


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all().order_by('-created')
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ReviewFilterSet
    ordering_fields = ['created']
    search_fields = ['name', 'description']
    pagination_class = DefaultPagination

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}


class CartItemViewSet(CreateRetrieveDestroyGenericViewSet):
    queryset = CartItem.objects.prefetch_related(
        'cartitem').all().order_by('-created')
    serializer_class = CartItemSerializer


class CartViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartSerializer
        if self.request.method == 'PATCH':
            return UpdateCartSerializer
        return CartReviewItemSerializer

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}

    def get_queryset(self):
        return Cart.objects.filter(cart_id=self.kwargs['cart_pk']).select_related('product')


class CustomerView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        (customer, create) = Customer.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
