from django.db import models
from djmoney.models.fields import MoneyField
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
    slug = models.SlugField(max_length=255, unique=True,
                            verbose_name='نامک', allow_unicode=True)
    price = MoneyField(decimal_places=2, verbose_name='قیمت واحد',
                       default_currency='IRR', max_digits=50)
    collection = models.ForeignKey(
        'Collection', on_delete=models.CASCADE, related_name='collection_item', verbose_name='مجموعه')
    promotion = models.ManyToManyField(
        'Promotion', related_name='promotion_item', verbose_name='تبلیغات', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصولی'
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
        verbose_name = 'مشتری'
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
        return f'{self.customer}'

    class Meta:
        verbose_name = 'وضعیت سفارشی'
        verbose_name_plural = 'وضعیت سفارشات'
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
        verbose_name = 'ادرسی'
        verbose_name_plural = 'ادرس مشتریان'
        ordering = ['-created']


class Collection(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True, verbose_name='شناسه')
    created = models.DateField(auto_now_add=True, verbose_name='ایجاد شده')
    title = models.CharField(max_length=255, unique=True, verbose_name='عنوان')
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, blank=True, related_name='featured_item', verbose_name='محصول ویژه')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مجموعه ای'
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

    def __str__(self):
        return f'{self.product} - {self.price}'

    class Meta:
        verbose_name = 'سفارشی'
        verbose_name_plural = 'سفارشات'
        ordering = ['-created']


class Cart(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True, verbose_name='شناسه')
    created = models.DateField(auto_now_add=True, verbose_name='ایجاد شده')
    product = models.ForeignKey(
        'Product', on_delete=models.PROTECT, related_name='product_item', verbose_name='محصول')
    quantity = models.PositiveSmallIntegerField(verbose_name='تعداد')

    def __str__(self):
        return f'{self.product} - {self.quantity}'

    class Meta:
        verbose_name = 'سبد خریدی'
        verbose_name_plural = 'سبد خرید'
        ordering = ['-created']


class Promotion(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True,
                          editable=False, unique=True, verbose_name='شناسه')
    created = models.DateField(auto_now_add=True, verbose_name='ایجاد شده')
    description = models.CharField(max_length=255, verbose_name='توضیحات')
    discount = models.FloatField(verbose_name='تخفیف')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'تبلیغی'
        verbose_name_plural = 'تبلیغات'
