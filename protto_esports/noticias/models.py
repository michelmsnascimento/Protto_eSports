from datetime import date
from django.db import models

# Create your models here.
class News(models.Model):
    idNews = models.IntegerField()
    game = models.CharField(max_length=128)
    date = models.DateField()
    name = models.CharField(max_length=128)
    text = models.TextField()
    image = models.CharField(max_length=200)
    like = models.IntegerField()

    def __str__(self):
        return self.name
   
    
class Comment(models.Model):
    idNews = models.IntegerField()
    idComment = models.IntegerField()
    userName = models.CharField(max_length=128)
    msg = models.TextField()
    
class Response(models.Model):
    idComment = models.IntegerField()
    userName = models.CharField(max_length=128)
    msgResp = models.TextField()