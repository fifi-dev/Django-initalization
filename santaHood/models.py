from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to = "santaHood/static/santaHood/img/", null=True, blank=True)
    alt = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField()
    last_modified = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name