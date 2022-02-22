from django.conf import settings
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    created_date = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_date']

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_date']


