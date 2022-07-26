from email.quoprimime import body_check
from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(user, related_name='posts', on_delete=models.CASCADE)

class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(user, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

class Like(models.Model):
    user = models.ForeignKey(user, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)