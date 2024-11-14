from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_coordinator = models.BooleanField("is coordinator", default=False)
    branch = models.CharField(max_length=200, default = "")
    library_ID = models.CharField(max_length=200, default = "")
    github = models.CharField(max_length=200, default = "")
    events_created = models.CharField(max_length=200, blank=True, default = "")
    events_participated = models.CharField(max_length=200, blank=True, default = "")

