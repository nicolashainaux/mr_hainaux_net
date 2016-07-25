from django.db import models

from .category import Category

class Theme(models.Model):
    order = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # content = models.TextField()

    def __str__(self):
        return self.category.name + ': ' + self.name

