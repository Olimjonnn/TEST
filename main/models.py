from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    barcode = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Deliver(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)

class ProductItem(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    deliver_id = models.ForeignKey(Deliver, on_delete=models.CASCADE)
    base_price = models.IntegerField()
    price = models.IntegerField()
    expired = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

