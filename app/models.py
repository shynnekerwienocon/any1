from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

class Client(models.Model):
    clientId = models.AutoField(primary_key=True)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    def __int__(self):
        return self.clientId

class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, default='Pending')

    def __str__(self):
        return f'Order {self.orderId} by {self.client}'

class Shipment(models.Model):
    shipmentId = models.AutoField(primary_key=True)
    order = models.OneToOneField('Order', on_delete=models.CASCADE)
    shipped_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    tracking_number = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'Shipment {self.shipmentId} for Order {self.order.orderId}'


