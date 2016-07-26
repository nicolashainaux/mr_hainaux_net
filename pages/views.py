from django.shortcuts import render_to_response
# from django.http import HttpResponse

from pages.models import Category, Theme


def home(request):
    return category(request, category='accueil')


def category(request, **kwargs):
    # todo: check the category does exist
    cat = kwargs.get('category', '')
    # todo: check a result at least is returned (otherwise return a 404)
    active_category = Category.objects.filter(slug__exact=cat)[0]
    navbar_links = [o.slug for o in Category.objects.all().order_by('order')]
    navbar_entries = [o.name for o in Category.objects.all().order_by('order')]
    navbar_infos = zip(navbar_links, navbar_entries)
    leftmenu_links = [o.slug
                      for o in Theme.objects.filter(
                          category_id=active_category.id).order_by('order')]
    leftmenu_entries = [o.name
                        for o in Theme.objects.filter(
                            category_id=active_category.id).order_by('order')]
    leftmenu_infos = zip(leftmenu_links, leftmenu_entries)
    return render_to_response('layout.html',
                              {'navbar_infos': navbar_infos,
                               'leftmenu_infos': leftmenu_infos,
                               'active': cat,
                               'content': active_category.text,
                               'test_var': navbar_links,
                               })


def theme(request, **kwargs):
    pass
