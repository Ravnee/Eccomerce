from django.db import models
from more_itertools import first
import datetime
# Create your models here.
class contact_info(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email =  models.EmailField(max_length=254)
    gender = models.CharField(max_length=10) 
    user_password = models.CharField(max_length=255)

    def __str__(self):
        return self.email


class admin_login(models.Model):
    admin_username = models.CharField(max_length=40)
    admin_password= models.CharField(max_length=40)

    def __str__(self):
        return self.admin_username

class Category(models.Model):
    name = models.CharField(max_length=50)  

    def __str__(self):
          return self.name


class product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='upload/product')
    price = models.IntegerField(default=100)
    description = models.CharField(max_length=255, default="good")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

class order(models.Model):
    product = models.ForeignKey(product, on_delete = models.CASCADE)
    customer = models.ForeignKey(contact_info, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default="",blank=True)
    phone = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)