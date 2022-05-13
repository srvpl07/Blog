from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'publish')
    Title = models.TextField()
    Body = models.TextField()
    Created_At = models.DateTimeField(default=timezone.now)
    Updated_At = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('Title',)

    def __str__(self):
        return self.Title