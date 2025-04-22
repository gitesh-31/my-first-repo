from datetime import date
from django.db import models

# Create your models here.


class book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(default="no dscription yet")
    published_date = models.DateField(default=date.today)
    pages = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} by {self.author}"
