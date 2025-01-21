from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)

    def __str__(self):
        return f'Профиль {self.user.username}'


class Course(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='Общая')
    short_description = models.TextField()
    full_description = models.TextField()
    content = models.TextField(null=True)

    users = models.ManyToManyField(User, related_name='courses', blank=True)

    def __str__(self):
        return self.title