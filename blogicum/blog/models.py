from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField()
    is_published = models.BooleanField(True)
    created_at = models.DateTimeField(auto_now_add=True)


class Location(models.Model):
    name = models.CharField(max_length=256)
    is_published = models.BooleanField(True)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )
    is_published = models.BooleanField(True)
    created_at = models.DateTimeField(auto_now_add=True)

