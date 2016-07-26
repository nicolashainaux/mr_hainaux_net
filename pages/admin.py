from django.contrib import admin

from .models import Category, Theme, Thumbnail

admin.site.register(Category)
admin.site.register(Theme)
admin.site.register(Thumbnail)
