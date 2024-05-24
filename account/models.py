from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    are_you_teacher = models.BooleanField(default=False)
    receive_newsletter = models.BooleanField(default=True)
    receive_notifications = models.BooleanField(default=True)

