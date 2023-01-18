from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id',  'title', 'price', 'collection']

    collection = SerializerMethodField()

    def get_collection(self, product: Product):
        return product.collection.title


class ProductCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
