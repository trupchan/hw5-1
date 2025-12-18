from django.contrib.auth.models import User
from django.db import models
import random

def generate_confirmation_code():
    return str(random.randint(100000, 999999))

class UserConfirmation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='confirmation')
    code = models.CharField(max_length=6, default=generate_confirmation_code)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.code}"