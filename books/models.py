from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=50)
    stock = models.CharField(max_length=200)
    description = models.TextField()
    upc = models.CharField(max_length=50)
    num_reviews = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    manually_added = models.BooleanField(default=False)

    def __str__(self):
        return self.title

