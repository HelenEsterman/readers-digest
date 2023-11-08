from django.db import models


class BookCategory(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name='bookCategories')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='bookCategories')
    date = models.DateTimeField(auto_now_add=True)
    