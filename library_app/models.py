import uuid
from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    publisher = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    copies = models.IntegerField()
    available = models.IntegerField(default=1)
    status = models.CharField(max_length=20, default="Available")

    def __str__(self):
        return f"{self.title} by {self.author}"
