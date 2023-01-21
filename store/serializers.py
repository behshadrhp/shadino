from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Product, Collection, Review, Cart


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
        fields = ['id', 'name', 'description', 'created']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
