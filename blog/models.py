from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

class Tag(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    def __str__(self):
        return self.slug


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)

class Entry(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        reverse("blog_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created_at"]
