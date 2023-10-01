from django.db import models


    
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