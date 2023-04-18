from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    decription = models.TextField()
    rate = models.FloatField()
    created_date = models.DateField(auto_now=True)
    modified_date = models.DateField(auto_now_add=True)

def __str__(self):
    return self.title

class Comment(models.Model):
    text = models.CharField(max_length=256)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
