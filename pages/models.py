from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    order = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, default=slugify(name))
    text = models.TextField()

    def __str__(self):
        return self.name


class Theme(models.Model):
    order = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, default=slugify(name))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category.name + ': ' + self.name


class Thumbnail(models.Model):
    order = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return str(self.theme) + ': ' + self.name
