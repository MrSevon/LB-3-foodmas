from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Bouquets(models.Model):
    categories = models.ManyToManyField(Category, related_name='bouquets')
    image = models.ImageField("Изображение", upload_to="bouquets/")
    price = models.IntegerField('Цена')
    title = models.CharField('Название', max_length=40)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'

class Orders(models.Model):
    name = models.CharField('Имя клиента', max_length=50)
    telephone = models.CharField('Номер телефона', max_length=15)
    adress = models.CharField('Адрес', max_length=100)
    comments = models.CharField('Пожелания к заказу', max_length=100)

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        return sum(item.bouquet.price * item.quantity for item in self.items.all())

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class OrderItem(models.Model):
    order = models.ForeignKey('Orders', on_delete=models.CASCADE, related_name='items')
    bouquet = models.ForeignKey('Bouquets', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.bouquet.title} x {self.quantity}"