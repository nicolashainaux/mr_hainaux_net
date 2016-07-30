import requests
from django.shortcuts import render_to_response
from django.http import HttpResponse

from pages.models import Category, FooterCategory, Theme, Tile
from .tools import get_client_ip


def home(request):
    return build(request, category='accueil')


def build(request, category='', theme=''):
    # todo: ? check the category does exist
    category_slug = category
    footer = False
    get_category_object = Category.objects.filter(slug__exact=category_slug)
    if len(get_category_object):
        category_object = get_category_object[0]
    else:
        get_footer = FooterCategory.objects.filter(slug__exact=category_slug)
        if len(get_footer):
            footer_object = get_footer[0]
            footer = True
        else:
            # todo: return a 404
            pass

    if footer:
        active_object = footer_object
    else:
        active_object = category_object

    navbar_links = ['/' + o.slug + '/'
                    for o in Category.objects.all().order_by('order')]
    navbar_links[0] = "/"
    navbar_entries = [o.name
                      for o in Category.objects.all().order_by('order')]
    navbar_infos = zip(navbar_links, navbar_entries)

    footer_links = [o.slug
                    for o in FooterCategory.objects.all().order_by('order')]
    footer_entries = [o.name
                      for o in FooterCategory.objects.all().order_by('order')]
    footer_infos = zip(footer_links, footer_entries)

    if footer:
        leftmenu_infos = []
    else:
        leftmenu_links = ['/' + o.category.slug + '/' + o.slug
                          for o in Theme.objects.filter(
                              category_id=category_object.id)
                          .order_by('order')]
        leftmenu_entries = [o.name
                            for o in Theme.objects.filter(
                                category_id=category_object.id)
                            .order_by('order')]
        leftmenu_infos = zip(leftmenu_links, leftmenu_entries)

    # todo: ? check the theme does exist
    theme_slug = theme
    active_theme = ''
    tiles_contents = []
    if theme_slug != '':
        # todo: check a result at least is returned (otherwise return a 404)
        theme_object = Theme.objects\
            .filter(slug__exact=theme_slug)\
            .filter(category_id=category_object.id)[0]
        active_theme = theme_object.name
        tiles_contents = [o.content
                          for o in Tile.objects.filter(
                              theme_id=theme_object.id).order_by('order')]

    return render_to_response('layout.html',
                              {'navbar_infos': navbar_infos,
                               'leftmenu_infos': leftmenu_infos,
                               'active_category': active_object.name,
                               'category_content': active_object.text,
                               'active_theme': active_theme,
                               'tiles_contents': tiles_contents,
                               'footer_infos': footer_infos,
                               'test_var': navbar_links,
                               })


def sheet(request, sheetname='', filename=''):
    r = requests.get('http://127.0.0.1:9999',
                     params={'sheetname': sheetname,
                             # 'ip': get_client_ip(request)
                             })
    if r.status_code == 200:
        response = HttpResponse(r.content,
                                content_type=r.headers['content-type'])
        response['Content-Disposition'] = \
            'attachment; filename="' + str(filename) + '.pdf"'
        return response
    else:
        response = HttpResponse(r.text)
        response.status_code = r.status_code
        return response
