from django.db import models

# Create your models here.
class PostNews(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to="post_news")
    Description = models.TextField()
    link = models.TextField(default="#")



class ImageNews(models.Model):
    image = models.ImageField(upload_to="post_news/details")
    post = models.ForeignKey(PostNews, on_delete=models.CASCADE)
