from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn_number = models.CharField(max_length=13, null=True, blank=True)
    cover_image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField("Category", through='BookCategory', related_name="books")