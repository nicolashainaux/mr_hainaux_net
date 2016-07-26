from django.contrib import admin

from .models import Category, Theme, Thumbnail


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Theme)
admin.site.register(Thumbnail)
