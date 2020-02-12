from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True) # can for example be used for book recommendations down the line? Seemed like a good idea, and it is a good test for seeing if the custom model works in any case :-)



