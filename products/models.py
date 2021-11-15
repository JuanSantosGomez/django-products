from django.db import models

# Create your models here.
class Product(models.Model):
    barcode = models.BigIntegerField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.description
