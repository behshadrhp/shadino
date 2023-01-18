from django.shortcuts import get_object_or_404
from django.db.models import ProtectedError
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Collection, Review
from .serializers import ProductSerializer, ProductCreateUpdateSerializer, CollectionSerializer, CollectionCreateUpdateSerializer, ReviewSerializer

# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('-updated')
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

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

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}