from django.db import models

# Create your models here.
class cnt(models.Model):
    name=models.TextField()
    phone=models.IntegerField()
    email=models.EmailField()
    msg=models.TextField()