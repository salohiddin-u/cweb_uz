from django.db import models

# Create your models here.
class UrlMapping(models.Model):
    long_url = models.CharField(max_length=250)
    short_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.short_id