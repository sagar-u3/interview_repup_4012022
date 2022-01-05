from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=50)
    stage = models.IntegerField(choices=[(1,1),(2,2),(3,3)])