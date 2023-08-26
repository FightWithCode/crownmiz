from django.db import models
from categories.models import Category

STATUS = (
    ("active", "Active"),
    ("draft", "Draft"),
)

def get_list_default():
    return []

class Artist(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    dob = models.DateField()
    new_worth = models.IntegerField()
    spouse = models.CharField(max_length=255, default=None, null=True, blank=True)
    summary = models.TextField(default=None, null=True, blank=True)
    also_known_as = models.CharField(max_length=255, default=None, null=True, blank=True)
    real_name = models.CharField(max_length=255, default=None, null=True, blank=True)
    nationality = models.CharField(max_length=255, default=None, null=True, blank=True)
    occupation = models.CharField(max_length=255, default=None, null=True, blank=True)
    years_active = models.CharField(max_length=255, default=None, null=True, blank=True)
    birth_place = models.CharField(max_length=255, default=None, null=True, blank=True)
    status = models.CharField(max_length=255, choices=STATUS, default="active")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    banner_image = models.ImageField(upload_to='artists', null=True, blank=True, default=None)
    thumbnail_image = models.ImageField(upload_to='artists', null=True, blank=True, default=None)
    featured_image = models.ImageField(upload_to='artists', null=True, blank=True, default=None)
    sign_image = models.ImageField(upload_to='artists', null=True, blank=True, default=None)
    facebook = models.CharField(max_length=255, default=None, null=True, blank=True)
    instagram = models.CharField(max_length=255, default=None, null=True, blank=True)
    twitter = models.CharField(max_length=255, default=None, null=True, blank=True)
    childrens = models.JSONField(default=get_list_default, null=True, blank=True)
    relatives = models.JSONField(default=get_list_default, null=True, blank=True)
    relationships = models.JSONField(default=get_list_default, null=True, blank=True)
    awards = models.JSONField(default=get_list_default, null=True, blank=True)
    other_details = models.JSONField(default=get_list_default, null=True, blank=True)
    did_you_know = models.JSONField(default=get_list_default, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

    def __str__(self):
        return self.name

