from django.db import models

# Create your models here.
class ImageInfo(models.Model):
    key = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    def __str__(self):
        return self.url
