from django.db import models
# Create your models here.

class Post(models.Model):
     post_title = models.CharField(max_length=1000)
     videofile = models.FileField(upload_to='videos/', blank=True, default='default.mp4')

     # post_body = models.TextField(default='', blank=True)
     image = models.ImageField(blank=True, default='default.jpg')

     def __str__(self):
          return self.post_title