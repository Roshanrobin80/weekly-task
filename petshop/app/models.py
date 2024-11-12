from django.db import models

# Create your models here.
class Pets(models.Model):
    pet_id=models.TextField()
    pet_type=models.TextField()
    pet_breed=models.TextField()
    pet_price=models.IntegerField()
    offer_price=models.IntegerField()
    img=models.FileField()
    dis=models.TextField()