from django.db import models

# Create your models here.
class loadimage(models.Model):
    name = models.CharField(max_length=50)
    Main_Img = models.ImageField(upload_to='images/')
