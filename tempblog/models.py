from django.db import models
from django.contrib.auth.models import User

class PersonalBlog(models.Model):
    title  = models.CharField(max_length=40)
    author =models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    body =models.TextField(max_length=1500)
    image =models.ImageField(upload_to='images/', null=True)
    def __str__(obj):
      return obj.title +' | '+ str(obj.author)
   