from django.db import models
from django.contrib.auth.models import User


class UserConfirmation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    secret_code = models.IntegerField()

    def __str__(self):
        return f"{self.secret_code}"