from django.db import models

# Create your models here.
class Film(models.Model):
    naslov = models.CharField(max_length=120)
    sadrzaj = models.TextField()
