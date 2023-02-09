from rest_framework.serializers import ModelSerializer, SerializerMethodField, UUIDField, ValidationError
from .models import Product, Collection, Review, Cart, CartItem, Customer


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


class CartReviewItemSerializer(ModelSerializer):
    product = ProductSerializer()
    total_price = SerializerMethodField()

    def get_total_price(self, cart: Cart):
        return int(cart.product.price.amount * cart.quantity)

    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity', 'total_price', 'created']


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


class AddCartSerializer(ModelSerializer):
    product_id = UUIDField()

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise ValidationError('هیچ محصولی با این شناسه کاربری یافت نشد')
        return value

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:
            cart_item = Cart.objects.get(
                cart_id=cart_id, product_id=product_id)
            # update an item
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except Cart.DoesNotExist:
            # Create New item
            self.instance = Cart.objects.create(
                cart_id=cart_id, **self.validated_data)
        return self.instance

    class Meta:
        model = Cart
        fields = ['id', 'product_id', 'quantity']


class UpdateCartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ['quantity']


class CustomerSerializer(ModelSerializer):
    user_id = UUIDField(read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'phone',
                  'birthday', 'membership', 'created']
