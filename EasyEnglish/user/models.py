from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ranking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points=models.IntegerField()

    def __str__(self):
        return '%s' % self.user