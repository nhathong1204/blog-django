from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog_Post(models.Model):
    image = models.ImageField(upload_to='img')
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField()
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    commenter = models.CharField(max_length=50)
    body = models.TextField()
    post = models.ForeignKey(Blog_Post, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self) -> str:
        return self.body