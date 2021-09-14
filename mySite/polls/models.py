from django.db import models
from django.db.models.fields import BooleanField, CharField, FloatField


# Create your models here.



class Login(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=255)

    def __str__(self) :
        return self.username


class Categories(models.Model):
    category_name = CharField(max_length=255)
    category_in = CharField(max_length=255,null=True)

    def __str__(self) :
        return self.category_name

class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_name = CharField(max_length=255)
    price = FloatField(default=0)
    discription = CharField(max_length=1000)
    url_images = CharField(max_length=1000)
    taitle = CharField(max_length=1000)
    status = BooleanField()

    def __str__(self) :
        id = str(self.id)
        return id

class Cart(models.Model):
    username = models.CharField(max_length=50,primary_key=True)
    item = models.TextField()

    def __str__(self) :
        return self.username