from django.db import models

# Create your models here.

class BookList(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Productlist(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    brand = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    
    def __str__(self):
        return self.title