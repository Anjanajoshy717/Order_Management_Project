from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES=(('admin','Admin'),('customer','Customer'))
    role=models.CharField(max_length=20,choices=ROLE_CHOICES)

    def __str__(self):
        return self.username

class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES=(('pending','Pending'),('completed','Completed'),('cancelled','Cancelled'),)
    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')

    def total_amount(self):
        total = 0
        for item in self.items.all():
            total += item.price * item.quantity
        return total

    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def subtotal(self):
        return self.price * self.quantity

    def __str__(self):
        return self.product.name