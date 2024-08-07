from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    
class List(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    project = models.ForeignKey(List, related_name='task', on_delete=models.CASCADE)
    name = models.CharField(max_length=155)
    description = models.TextField
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name