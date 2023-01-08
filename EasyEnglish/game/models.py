from django.db import models

# Create your models here.


class Hangman(models.Model):
    TYPES=[('Animal', 'Animal'),('Food','Food'), ('Furniture', 'Furniture'), ('School material', 'School material')]

    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TYPES)
    spanish = models.CharField(max_length=100)
    photo = models.ImageField(null=True)

    def __str__(self):
        return '%s' % self.word

