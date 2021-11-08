from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=400)
   
    def __str__(self):
        return self.title
    

class Order(models.Model):
    items= models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email= models.EmailField(max_length=140)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    total = models.CharField(max_length= 200)
    
    def __str__(self):
        return self.name
    
    
    