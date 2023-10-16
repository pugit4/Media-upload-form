from django.db import models

# Create your models here.
class resume(models.Model):
    name = models.CharField(max_length=25)
    cv = models.FileField(upload_to='upload/')
    image = models.ImageField(upload_to='images/')