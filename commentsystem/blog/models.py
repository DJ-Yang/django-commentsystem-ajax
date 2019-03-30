from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.CharField(max_length=240)

class Comment(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', default=None, on_delete=models.PROTECT, null=True)
    body = models.CharField(max_length=240)