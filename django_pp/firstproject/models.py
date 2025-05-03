from django.db import models

MAX_LENGTH = 255

class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Tag(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название тега')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Product(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название товара')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='furniture/%Y/%m/%d', null=True, blank=True, verbose_name='Картинка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_deleted = models.BooleanField(default=False, verbose_name='Логическое удаление')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True, related_name='products', verbose_name='Теги')

    def __str__(self):
        return f"{self.name} — {self.price} руб."

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Order(models.Model):
    number = models.CharField(max_length=20, unique=True, verbose_name='Уникальный номер заказа')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    delivery_address = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес доставки')
    client_phone = models.CharField(max_length=20, verbose_name='Телефон клиента')
    client_full_name = models.CharField(max_length=MAX_LENGTH, verbose_name='ФИО клиента')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='Скидка за единицу')

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'
