from django.db import models
from artists.models import Artist
from categories.models import Category

STATUS = (
    ("active", "Active"),
    ("draft", "Draft"),
)

def get_list_default():
    return []

class Movie(models.Model):
    name =  models.CharField(max_length=255)
    slug =  models.CharField(max_length=255)
    starring = models.ManyToManyField(Artist)
    release_data = models.DateField(default=None, null=True, blank=True)
    summary = models.TextField(default=None, blank=True, null=True)
    performance = models.TextField(default=None, blank=True, null=True)
    hightlights = models.TextField(default=None, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    banner_image = models.ImageField(upload_to='artists', null=True, blank=True, default=None)
    thumbnail_image = models.ImageField(upload_to='artists', null=True, blank=True, default=None)
    featured_image = models.ImageField(upload_to='artists', null=True, blank=True, default=None)
    status = models.CharField(max_length=255, choices=STATUS, default="active")
    genere = models.CharField(max_length=255, default=None, null=True, blank=True)
    tags = models.JSONField(default=get_list_default, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Song(models.Model):
    name =  models.CharField(max_length=255)
    slug =  models.CharField(max_length=255)
    singer = models.ManyToManyField(Artist, related_name='singer')
    musician = models.ManyToManyField(Artist, related_name='musician')
    lyricist = models.ManyToManyField(Artist, related_name='lyricist')
    release_date = models.DateField(default=None, null=True, blank=True)
    summary = models.TextField(default=None, blank=True, null=True)
    lyrics = models.TextField(default=None, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    status = models.CharField(max_length=255, choices=STATUS, default="active")
    banner_image = models.ImageField(upload_to='artists', null=True, blank=True, default=None)
    thumbnail_image = models.ImageField(upload_to='artists', null=True, blank=True, default=None)
    featured_image = models.ImageField(upload_to='artists', null=True, blank=True, default=None)
    youtube = models.URLField(default=None, null=True, blank=True)
    online_streamings = models.JSONField(default=get_list_default, null=True, blank=True)
    tags = models.JSONField(default=get_list_default, null=True, blank=True)
    keywords = models.JSONField(default=get_list_default, null=True, blank=True)
    meta_title = models.CharField(max_length=255, default=None, null=True, blank=True)
    meta_desc = models.JSONField(default=get_list_default, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

