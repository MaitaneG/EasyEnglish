from django.db import models
from django.contrib.auth.models import User

from vocabulary.models import Term

# Create your models here.
class Ranking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points=models.IntegerField()
    learnt=models.ManyToManyField(Term)

    def __str__(self):
        return '%s' % self.user