from django.db import models

from apps.users.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    desc = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.category.name
    
class ProType(models.Model):
    type = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200, null=True, blank=True)
    size = models.PositiveBigIntegerField()
    price = models.PositiveBigIntegerField()
    discount = models.PositiveBigIntegerField(null=True, blank=True)
    def __str__(self):
        return self.name

#############################################

# About card store 

class Cart(models.Model):
    completed = models.BooleanField(default=False)
    session_id = models.CharField(max_length=100)
    @property
    def num_of_items(self):
        cart_items = self.cart_items.all()
        return sum([i.quantity for i in cart_items])
    @property
    def cart_total(self):
        cart_items = self.cart_items.all()
        return sum([i.subtotal for i in cart_items])
    def __str__(self):
        return str(self.session_id)


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')

    def __str__(self):
        if self.phone_number:
            return f"{self.phone_number}"
        return self.user.username

    @property
    def num_of_items(self):
        cart_items = self.order_items.all()
        return sum([i.quantity for i in cart_items])

    @property
    def cart_total(self):
        cart_items = self.order_items.all()
        return sum([i.subtotal for i in cart_items])


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True, related_name="cart_items")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    # product_image = models.ForeignKey(ProductImage, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.ForeignKey(ProType, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity}'

    # @property
    # def subtotal(self):
    #     return round(self.quantity * (
    #             self.product_image.price_uzs + ((self.variant.percent * self.product_image.price_uzs) / 100)), 2)
    
    
#############################################

class Image(models.Model):
    name = models.ForeignKey(ProType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return str(self.image)

class Master(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
    
class ImageService(models.Model):
    name = models.ForeignKey(Service, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image-service/')
    def __str__(self):
        return str(self.image)

class Marketing(models.Model):
    market = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images/', null=True, blank=True)
    social = models.CharField(max_length=200)
    def __str__(self):
        return self.contact