from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    datr_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Project(models.Model):
    name_project = models.CharField(max_length=50, unique=True)
    application_area = models.TextField(max_length=100)
    production_cycle = models.TextField(max_length=50)
    target_audience = models.TextField(max_length=50)

    def get_absolute_url(self):
        return reverse('project_justification_detail_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('project_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('project_delete_url', kwargs={'id': self.id})

    def __str__(self):
        return self.name_project


class News(models.Model):
    news = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('news_detail_url', kwargs={'id': self.id})

    def __str__(self):
        return self.news
