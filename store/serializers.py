from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Product, Collection, Review, Cart, CartItem


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
        fields = ['product', 'quantity', 'total_price', 'created']

    product = ProductSerializer()
    total_price = SerializerMethodField()

    def get_total_price(self, cart: Cart):
        return int(cart.product.price.amount * cart.quantity)


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'cartitem', 'total_price', 'created']

    cartitem = CartSerializer(many=True)
    total_price = SerializerMethodField()

    def get_total_price(self, cart: CartItem):
        result = sum(
            [item.quantity * item.product.price.amount for item in cart.cartitem.all()])
        return int(result)

    def create(self, validated_data):
        items_data = validated_data.pop('cartitem')
        cart = Cart.objects.create(**validated_data)
        return cart
