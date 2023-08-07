from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    description= models.CharField(max_length=200)
    content=models.TextField()
    creation_date=models.DateTimeField(auto_now_add=True)
    name=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    likecount=models.IntegerField(null=True)
    
    
    def __str__(self):
        return self.title
    
    
    
class like(models.Model):
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    

    















created=models.DateTimeField(auto_now_add=True)