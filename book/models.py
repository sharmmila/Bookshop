from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return f"{self.title}"


class Book(models.Model):
    image = models.ImageField(upload_to='book_photos/', null=True, blank=True)
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    rate = models.FloatField(default=0)
    tags = models.ManyToManyField(
        Tag,
        related_name='books',
        blank=True
    )
    categories = models.ManyToManyField(Category,
                                        related_name='books',
                                        blank=True)

    def __str__(self):
        return f"{self.title}"


class Reviews(models.Model):
    text = models.TextField()
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text}"

