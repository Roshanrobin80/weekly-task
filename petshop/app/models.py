from django.db import models

# Create your models here.
class Pets(models.Model):
    pet_id=models.TextField()
    type=models.TextField()
    breed=models.TextField()
    price=models.IntegerField()
    img=models.FileField()
    dis=models.TextField()