from django.db import models
from django.urls import reverse


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(default=' ',)
    image = models.ImageField(upload_to = "santaHood/static/santaHood/img/", )
    alt = models.CharField(max_length=50, null=False)
    quantity = models.IntegerField()
    last_modified = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name