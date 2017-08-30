from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    order = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)
    html_name = models.CharField(max_length=100, default='unset')
    slug = models.SlugField(max_length=100, default='unset')
    text = models.TextField()

    def __str__(self):
        return self.name


class FooterCategory(models.Model):
    class Meta:
        verbose_name_plural = "footer categories"
    order = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)
    html_name = models.CharField(max_length=100, default='unset')
    slug = models.SlugField(max_length=100, default='unset')
    text = models.TextField()

    def __str__(self):
        return self.name


class Theme(models.Model):
    order = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)
    html_name = models.CharField(max_length=100, default='unset')
    slug = models.SlugField(max_length=100, default='unset')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category.name + ': ' + self.name


class News(models.Model):
    class Meta:
        verbose_name_plural = "news"
    date = models.DateField(auto_now_add=True)
    published_on_home_page = models.BooleanField(default=True)
    title = models.CharField(max_length=100)
    html_title = models.CharField(max_length=100, default='unset')
    content = models.TextField(blank=True)

    def __str__(self):
        return str(self.date) + '_' + self.title


class Tile(models.Model):
    order = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)
    html_name = models.CharField(max_length=100, default='unset')
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)
    content = models.TextField()

    def __str__(self):
        return str(self.theme) + ': ' + self.name
