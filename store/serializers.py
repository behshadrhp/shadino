from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Product, Collection, Review, Cart, CartItem


class ProductSerializer(ModelSerializer):
    collection = SerializerMethodField()

    def get_collection(self, product: Product):
        return product.collection.title

    class Meta:
        model = Product
        fields = ['id',  'title', 'price', 'collection']


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
    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)

    class Meta:
        model = Review
        fields = ['id', 'name', 'description', 'created']


class CartSerializer(ModelSerializer):
    product = ProductSerializer()
    total_price = SerializerMethodField()

    def get_total_price(self, cart: Cart):
        return int(cart.product.price.amount * cart.quantity)

    class Meta:
        model = Cart
        fields = ['product', 'quantity', 'total_price', 'created']


class CartItemSerializer(ModelSerializer):
    cartitem = CartSerializer(many=True, read_only=True)
    total_price = SerializerMethodField()

    def get_total_price(self, cart: CartItem):
        result = sum(
            [item.quantity * item.product.price.amount for item in cart.cartitem.all()])
        return int(result)

    class Meta:
        model = CartItem
        fields = ['id', 'cartitem', 'total_price', 'created']
