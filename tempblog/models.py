from django.db import models
from django.contrib.auth.models import User

class PersonalBlog(models.Model):
    blogtitle = models.CharField(max_length=40)
    blogauthor=models.ForeignKey(User,on_delete=models.CASCADE)
    blogbody=models.TextField(max_length=1500)

    def __str__(obj):
      return self.blogtitle +'|'+ str(self.blogauthor)
   