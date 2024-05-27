from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username+"'s cart"
    


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    listed_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="product_images", blank=True, null=True)
    
    carts = models.ManyToManyField(Cart, related_name="products")

    def __str__(self):
        return self.name


