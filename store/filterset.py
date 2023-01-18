from django_filters.rest_framework import FilterSet
from .models import Product, Review


class ProductFilterSet(FilterSet):
    class Meta:
        model = Product
        fields = {
            'collection_id': ['exact'],
            'price': ['gt', 'lt']
        }


class ReviewFilterSet(FilterSet):
    class Meta:
        model = Review
        fields = {
            'name': ['exact']
        }
