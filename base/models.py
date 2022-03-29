from django.db import models
from django.contrib.auth.models import User


class MainUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=110)

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=150)
    product_description = models.TextField(max_length=500)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_brand = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name

class Stats(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.date