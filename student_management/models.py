from django.db import models


# Create your models here.
class Image(models.Model):
    key = models.CharField(max_length=200, default="")
    img = models.ImageField(upload_to="images")
