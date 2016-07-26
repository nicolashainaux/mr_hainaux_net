from django.shortcuts import render_to_response
# from django.http import HttpResponse

from pages.models import Category, Theme, Thumbnail


def home(request):
    return build(request, category='accueil')


def build(request, category='', theme=''):
    # todo: ? check the category does exist
    category_slug = category
    # todo: check a result at least is returned (otherwise return a 404)
    category_object = Category.objects.filter(slug__exact=category_slug)[0]

    navbar_links = [o.slug for o in Category.objects.all().order_by('order')]
    navbar_entries = [o.name for o in Category.objects.all().order_by('order')]
    navbar_infos = zip(navbar_links, navbar_entries)

    leftmenu_links = ['/' + o.category.slug + '/' + o.slug
                      for o in Theme.objects.filter(
                          category_id=category_object.id).order_by('order')]
    leftmenu_entries = [o.name
                        for o in Theme.objects.filter(
                            category_id=category_object.id).order_by('order')]
    leftmenu_infos = zip(leftmenu_links, leftmenu_entries)

    # todo: ? check the theme does exist
    theme_slug = theme
    thumbnails = []
    if theme_slug != '':
        # todo: check a result at least is returned (otherwise return a 404)
        theme_object = Theme.objects\
            .filter(slug__exact=theme_slug)\
            .filter(category_id=category_object.id)[0]
        thumbnails = [o.content
                      for o in Thumbnail.objects.filter(
                          theme_id=theme_object.id).order_by('order')]

    return render_to_response('layout.html',
                              {'navbar_infos': navbar_infos,
                               'leftmenu_infos': leftmenu_infos,
                               'active_category': category_slug,
                               'content': category_object.text,
                               'active_theme': theme_slug,
                               'thumbnails': thumbnails,
                               'test_var': navbar_links,
                               })
