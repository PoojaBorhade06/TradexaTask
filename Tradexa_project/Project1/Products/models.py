from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=30)
    weight=models.FloatField(null=True)
    price=models.FloatField(null=True)
    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)