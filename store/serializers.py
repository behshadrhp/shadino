from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Product, Collection, Review


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


class CollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'created']


class CollectionCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description', 'product', 'created']