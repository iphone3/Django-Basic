from django.db import models

class News(models.Model):
    img = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)
    username = models.CharField(max_length=100)
