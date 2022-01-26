from django.contrib.auth.models import User
from django.db import models

# Create your models here.from


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateField()
    updated_at=models.DateField()