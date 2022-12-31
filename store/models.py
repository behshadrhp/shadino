from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from uuid import uuid4


# Create your models here.


class Product(models.Model):
    # product information

    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    collection = models.ForeignKey(
        'Collection', on_delete=models.CASCADE, related_name='collection_item')
    promotion = models.ManyToManyField(
        'Promotion', related_name='promotion_item')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'محصولات'
        ordering = ['-updated']


class Customer(models.Model):

    # membership choice
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICE = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]

    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True)
    created = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True, help_text='Contact phone number')
    birthday = models.DateField(default=datetime.now, editable=True)
    membership = models.CharField(
        max_length=1, default=MEMBERSHIP_BRONZE, choices=MEMBERSHIP_CHOICE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'مشتریان'
        ordering = ['birthday']


class Order(models.Model):

    # payment status
    PENDING_STATUS = 'P'
    COMPLETE_STATUS = 'C'
    FAILED_STATUS = 'F'
    PAYMENT_STATUS = [
        (PENDING_STATUS, 'Pending'),
        (COMPLETE_STATUS, 'Complete'),
        (FAILED_STATUS, 'Failed')
    ]

    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True)
    placed_at = models.DateField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS, default=PENDING_STATUS)
    customer = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, related_name='customer_item')

    def __str__(self):
        return self.placed_at

    class Meta:
        verbose_name_plural = 'وضعیت سفارش'
        ordering = ['-placed_at']


class Address(models.Model):
    customer = models.OneToOneField(
        'Customer', on_delete=models.CASCADE, primary_key=True)
    created = models.DateField(auto_now_add=True)
    city = models.CharField(max_length=25)
    street = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.customer} - {self.city}'

    class Meta:
        verbose_name_plural = 'ادرس مشتریان'
        ordering = ['-created']


class Collection(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True)
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255, unique=True)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='featured_item')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'مجموعه ها'
        ordering = ['-created']


class OrderItem(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True)
    created = models.DateField(auto_now_add=True)
    order = models.ForeignKey(
        'Order', on_delete=models.PROTECT, related_name='order_item')
    product = models.ForeignKey(
        'Product', on_delete=models.PROTECT, related_name='product_items')
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.product} - {self.price}'

    class Meta:
        verbose_name_plural = 'سفارشات'
        ordering = ['-created']


class Cart(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.created

    class Meta:
        verbose_name_plural = 'سبد ها'
        ordering = ['-created']


class CartItem(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True)
    created = models.DateField(auto_now_add=True)
    cart = models.ForeignKey(
        'Cart', on_delete=models.CASCADE, related_name='cart_item')
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='product_item')
    quantity = models.SmallIntegerField()

    class Meta:
        verbose_name_plural = 'سبد خرید'
        ordering = ['-created']


class Promotion(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True)
    created = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

    class Meta:
        verbose_name_plural = 'تبلیغات'
