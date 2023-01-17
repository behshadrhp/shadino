from django.shortcuts import get_object_or_404
from django.db.models import ProtectedError
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('updated')
    serializer_class = ProductSerializer


    def destroy(self, request, pk):
        queryset = get_object_or_404(Product, pk=pk)
        try:
            queryset.delete()
            return Response({'پیام':'محصول حذف شد'}, status=status.HTTP_200_OK)
        except ProtectedError:
            return Response({'پیام':'این محصول را نمی توان حذف کرد زیرا به یک سبد خرید مرتبط است'}, status=status.HTTP_406_NOT_ACCEPTABLE)
