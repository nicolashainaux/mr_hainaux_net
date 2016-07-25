from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    order = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.name

