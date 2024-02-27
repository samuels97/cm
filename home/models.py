from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=15)

class Bible(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter = models.IntegerField()
    verse = models.IntegerField()

