from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.charField(max_length=100)
    content = models.TextField()