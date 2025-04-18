from django.db import models
from django.urls import reverse
from accounts.models import CustomUser

# Create your models here.

class Article(models.Model):
  title = models.CharField(max_length=255)
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse("article_detail",kwargs={"pk" : self.pk})


class Comment(models.Model):
  article = models.ForeignKey(Article,on_delete=models.CASCADE)
  comment = models.CharField(max_length=140)
  author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

  def __str__(self):
    return self.comment
  
  def get_absolute_url(self):
    return reverse("article_detail")