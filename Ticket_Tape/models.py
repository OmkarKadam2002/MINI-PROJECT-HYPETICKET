from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    message = models.TextField(default='abc')

class Account(models.Model):
    name = models.TextField(default='abc')
    email_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    conpassword = models.CharField(max_length=100)
    number = models.CharField(max_length=100,default="")
    age = models.CharField(max_length=100,default="")
    location = models.TextField(default='abc')

class Review(models.Model):
    username = models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    review = models.TextField(default='abc')
    rating = models.FloatField()
    location = models.TextField(default='abc')
    created = models.DateTimeField(auto_now_add=True)

class Monument(models.Model):
    name = models.TextField(default='abc')
    location = models.TextField(default='abc')
    desc = models.TextField(default='abc')
    inst = models.TextField(default='abc')
    time = models.TextField(default='abc')
    reach = models.TextField(default='abc')
    location = models.TextField(default='abc')
    date = models.DateField(null=True)
    price_ind = models.TextField(default='abc')
    price_for = models.TextField(default='abc')

class Tickets(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    monument_name = models.TextField(default='abc')
    location = models.TextField(default='abc')
    count_ind = models.TextField(default='abc')
    count_for = models.TextField(default='abc')
    count_free = models.TextField(default='abc')
    price = models.TextField(default='abc')
    username=models.CharField(max_length=100,default='abc')
    qr_code=models.ImageField(upload_to='qr-codes',blank=True)

    

    


    


