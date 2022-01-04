from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

class Post(models.Model):
    title = models.CharField(max_length= 255)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    body = models.TextField(max_length= 70000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args = (str(self.id)))    

# Create your models here.
