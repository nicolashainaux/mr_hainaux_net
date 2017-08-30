from django.contrib import admin

from .models import Category, FooterCategory, Theme, Tile, News


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class FooterCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ThemeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class TileAdmin(admin.ModelAdmin):
    # list_display = ['title', 'published']
    # ordering = ['title']
    actions = ['make_published', 'make_unpublished']

    def _msg(self, nb_updated, as_what, request):
        if nb_updated == 1:
            msg = '1 tile was'
        else:
            msg = '{} tiles were'.format(nb_updated)
        self.message_user(request,
                          '{} successfully marked as {}.'.format(msg,
                                                                 as_what))

    def make_published(self, request, queryset):
        self._msg(queryset.update(published=True), 'published', request)

    def make_unpublished(self, request, queryset):
        self._msg(queryset.update(published=False), 'unpublished', request)

    make_published.short_description = 'Mark selected tiles as published'
    make_unpublished.short_description = 'Mark selected tiles as unpublished'


admin.site.register(Category, CategoryAdmin)
admin.site.register(FooterCategory, FooterCategoryAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Tile, TileAdmin)
admin.site.register(News)
