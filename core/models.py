from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    """Campo para o user colocar uma tarefa"""
    task = models.CharField(max_length=65)
    date_added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.task
