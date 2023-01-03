from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from uuid import uuid4


# Create your models here.


class Product(models.Model):
    # product information

    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True, verbose_name='شناسه')
    created = models.DateField(auto_now_add=True, verbose_name='ایجاد شده')
    updated = models.DateField(auto_now=True, verbose_name='به روز رسانی شده')
    title = models.CharField(max_length=255, unique=True, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیاحات')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='نامک')
    price = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name='قیمت واحد')
    collection = models.ForeignKey(
        'Collection', on_delete=models.CASCADE, related_name='collection_item', verbose_name='مجموعه')
    promotion = models.ManyToManyField(
        'Promotion', related_name='promotion_item', verbose_name='تبلیغات')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'محصولات'
        ordering = ['-updated']


class Customer(models.Model):

    # membership choice
    MEMBERSHIP_BRONZE = 'برنز'
    MEMBERSHIP_SILVER = 'نقره'
    MEMBERSHIP_GOLD = 'طلا'
    MEMBERSHIP_CHOICE = [
        (MEMBERSHIP_BRONZE, 'عضویت برنزی'),
        (MEMBERSHIP_SILVER, 'عضویت نقره ای'),
        (MEMBERSHIP_GOLD, 'عضویت طلای')
    ]

    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True, verbose_name='شناسه')
    created = models.DateField(auto_now_add=True, verbose_name='ایجاد شده')
    first_name = models.CharField(max_length=25, verbose_name='نام')
    last_name = models.CharField(max_length=25, verbose_name='نام خوانوادگی')
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    phone = PhoneNumberField(
        unique=True, help_text='لطفا شماره همراه خود را وارد کنید', verbose_name='شماره همراه')
    birthday = models.DateField(
        default=datetime.now, editable=True, verbose_name='تاریخ تولد')
    membership = models.CharField(
        max_length=5, default=MEMBERSHIP_BRONZE, choices=MEMBERSHIP_CHOICE, verbose_name='نوع عضویت')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'مشتریان'
        ordering = ['birthday']


class Order(models.Model):

    # payment status
    PENDING_STATUS = 'در انتظار'
    COMPLETE_STATUS = 'تکیمل'
    FAILED_STATUS = 'لغو عملیات'
    PAYMENT_STATUS = [
        (PENDING_STATUS, 'در انتظار پرداخت'),
        (COMPLETE_STATUS, 'پرداخت تکمیل شده است'),
        (FAILED_STATUS, 'لغو عملیات پرداخت')
    ]

    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True, verbose_name='شناسه')
    placed_at = models.DateField(auto_now_add=True, verbose_name='ایجاد شده')
    payment_status = models.CharField(
        max_length=15, choices=PAYMENT_STATUS, default=PENDING_STATUS, verbose_name='وضعیت پرداخت')
    customer = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, related_name='customer_item', verbose_name='مشتری')

    def __str__(self):
        return self.placed_at

    class Meta:
        verbose_name_plural = 'وضعیت سفارش'
        ordering = ['-placed_at']


class Address(models.Model):
    customer = models.OneToOneField(
        'Customer', on_delete=models.CASCADE, primary_key=True, verbose_name='مشتری')
    created = models.DateField(auto_now_add=True, verbose_name='ایجاد شده')
    city = models.CharField(max_length=25, verbose_name='شهر')
    street = models.TextField(max_length=200, verbose_name='خیابان')

    def __str__(self):
        return f'{self.customer} - {self.city}'

    class Meta:
        verbose_name_plural = 'ادرس مشتریان'
        ordering = ['-created']


class Collection(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True, verbose_name='شناسه')
    created = models.DateField(auto_now_add=True, verbose_name='ایجاد شده')
    title = models.CharField(max_length=255, unique=True, verbose_name='عنوان')
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='featured_item', verbose_name='محصول ویژه')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'مجموعه ها'
        ordering = ['-created']


class OrderItem(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True, verbose_name='شناسه')
    created = models.DateField(auto_now_add=True, verbose_name='ایجاد شده')
    order = models.ForeignKey(
        'Order', on_delete=models.PROTECT, related_name='order_item', verbose_name='سفارش')
    product = models.ForeignKey(
        'Product', on_delete=models.PROTECT, related_name='product_items', verbose_name='محصول')
    quantity = models.PositiveSmallIntegerField(verbose_name='تعداد')
    price = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name='قیمت واحد')

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
                          editable=False, unique=True, verbose_name='شناسه')
    created = models.DateField(auto_now_add=True, verbose_name='ایجاد شده')
    cart = models.ForeignKey(
        'Cart', on_delete=models.CASCADE, related_name='cart_item', verbose_name='سبد')
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='product_item', verbose_name='محصول')
    quantity = models.PositiveSmallIntegerField(verbose_name='تعداد')

    class Meta:
        verbose_name_plural = 'سبد خرید'
        ordering = ['-created']


class Promotion(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True, verbose_name='شناسه')
    created = models.DateField(auto_now_add=True, verbose_name='ایجاد شده')
    description = models.CharField(max_length=255, verbose_name='توضیحات')
    discount = models.FloatField(verbose_name='تخفیف')

    class Meta:
        verbose_name_plural = 'تبلیغات'
