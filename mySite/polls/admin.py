from django.contrib import admin
from django.db.models.fields import PositiveBigIntegerField
from .models import Login, Categories, Products, Cart
# Register your models here.



admin.site.register(Login)
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Cart)