from django.db import models


CATEGORY_TYPES = (
    ("song", "Song"),
    ("movie", "Movie"),
)

CATEGORY_STATUS = (
    ("active", "Active"),
    ("draft", "Draft"),
)

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=255, choices=CATEGORY_TYPES)
    status = models.CharField(max_length=255, choices=CATEGORY_STATUS, default="active")
    image = models.ImageField(upload_to='categories', null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
