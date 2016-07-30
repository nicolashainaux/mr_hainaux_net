from django.contrib import admin

from .models import Category, FooterCategory, Theme, Tile


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class FooterCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ThemeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(FooterCategory, FooterCategoryAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Tile)
