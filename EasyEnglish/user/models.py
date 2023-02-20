from django.db import models
from django.contrib.auth.models import User

from vocabulary.models import Term

# Create your models here.
class Ranking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points=models.IntegerField()
    learnts=models.ManyToManyField(Term,through='Learnt')

    def __str__(self):
        return '%s' % self.user

class Learnt(models.Model):
    user=models.ForeignKey(Ranking, on_delete=models.CASCADE)
    word=models.ForeignKey(Term, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.user , self.word)
    
    class Meta:
        unique_together=[['user', 'word']]