from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    
    def __str__(self):
        return self.text