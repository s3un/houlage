from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    license=models.CharField(default='xxx-xxx-xxx',max_length=50)
    picture = models.ImageField(upload_to="profile", default="profile/users.png")
    address = models.CharField(max_length=150, default="lagos")
    phone = models.CharField(max_length=150, default="08000012345")
    def __str__(self):
        return self.email

