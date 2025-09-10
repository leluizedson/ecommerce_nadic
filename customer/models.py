from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.Cascade)
    telefone = models.CharField(max_length=13, blank=True, null=True)

    
    def __str__(self):
        return self.user.username
