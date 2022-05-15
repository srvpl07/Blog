from django.db import models
from django.contrib.auth.models import User

class Accounts(models.Model):
    username = models.TextField()
    password = models.TextField()

