from atexit import register
from django.db import models
import datetime
from email.headerregistry import Address
from email.policy import default
from tables import Description

# Create your models here.
class contact_info(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.IntegerField()
    password=models.CharField(max_length=255)


class category(models.Model):
    name=models.CharField(max_length=50)

    def __str__ (self):
        return self.name
    
class products(models.Model):
    productname=models.CharField( max_length=50)
    image=models.ImageField(upload_to='uploads/images')
    price=models.IntegerField(default=100)
    description=models.CharField(max_length=225,default="good")
    category=models.ForeignKey(category,on_delete=models.CASCADE,default=1)

    def __str__ (self):
        return self.productname
    

class order(models.Model):
    product=models.ForeignKey(products, on_delete=models.CASCADE)
    customer=models.ForeignKey(contact_info, on_delete=models.CASCADE)
    quntity=models.IntegerField(default=1)
    price=models.IntegerField()
    Address=models.CharField(max_length=50,default="",blank=True)
    phone=models.IntegerField()
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def _str_(self):
        return self.Address

class restframework(models.Model):
    name=models.CharField( max_length=50)
    email=models.CharField(max_length=223)

    def __str__(self):
        return self.name

