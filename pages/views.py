from django.shortcuts import render_to_response
# from django.http import HttpResponse

from pages.models import Category, Theme


def home(request):
    return category(request, category='accueil')


def category(request, **kwargs):
    # todo: check the category does exist
    cat = kwargs.get('category', None)
    # todo: check a result at least is returned
    active_category = Category.objects.filter(slug__exact=cat)[0]
    navbar_links = [o.slug for o in Category.objects.all().order_by('order')]
    navbar_entries = [o.name for o in Category.objects.all().order_by('order')]
    navbar_infos = zip(navbar_links, navbar_entries)
    leftmenu_entries = [o.name
                        for o in Theme.objects.filter(
                            category_id=active_category.id).order_by('order')]
    return render_to_response('layout.html',
                              {'navbar_infos': navbar_infos,
                               'leftmenu_entries': leftmenu_entries,
                               'active': cat,
                               'content': active_category.text,
                               'test_var': navbar_links,
                               })


def theme(request, **kwargs):
    pass
