from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class UserReview(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name='userReviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userReviews')
    rating = models.IntegerField(blank=False,  # Set a default value for the field
        validators=[  # Add validators for custom validation rules
            MinValueValidator(1),  # Minimum value allowed
            MaxValueValidator(10),  # Maximum value allowed
        ])
    comment = models.CharField(max_length=500, blank=True)
    date = models.DateField()
    