from django.db import models

class Book(models.Model):
    image = models.ImageField(upload_to='book_photos/', null=True, blank=True)
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    rate = models.FloatField(default=0)

    def __str__(self):
        return f"{self.title}"