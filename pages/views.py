import requests
from django.http import Http404
from django.shortcuts import render_to_response
from django.http import HttpResponse

from pages.models import Category, FooterCategory, Theme, Tile, News
from .tools import get_client_ip, clean_list


def home(request):
    return build(request, category='accueil')


def build(request, category=''):
    # todo: ? check the category does exist
    if category == 'admin':
        raise Http404
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
        active_category = footer_object
    else:
        active_category = category_object

    navbar_slugs = [o.slug
                    for o in Category.objects.all().order_by('order')]
    navbar_links = ['/' + o.slug + '/'
                    for o in Category.objects.all().order_by('order')]
    navbar_links[0] = "/"
    navbar_entries = [o.name
                      for o in Category.objects.all().order_by('order')]
    navbar_data = zip(navbar_slugs, navbar_links, navbar_entries)

    footer_links = [o.slug
                    for o in FooterCategory.objects.all().order_by('order')]
    footer_entries = [o.name
                      for o in FooterCategory.objects.all().order_by('order')]
    footer_data = zip(footer_links, footer_entries)

    if footer:
        leftmenu_data = []
    elif active_category.slug == 'calcul-mental':
        leftmenu_titles = [' '.join(o.name.split()[:2])
                           for o in Theme.objects.filter(
                               category_id=category_object.id)
                           .order_by('order')]
        leftmenu_titles = clean_list(leftmenu_titles)
        leftmenu_data = []
        for t in leftmenu_titles:
            # [(complete link, theme slug, theme name, entry name)]
            leftmenu_infos = [('/' + thm.category.slug + '/' + thm.slug,
                               thm.slug,
                               thm.name,
                               ' '.join(thm.name.split()[-2:]))
                              for thm in Theme.objects.filter(
                                  category_id=category_object.id)
                              .order_by('order')
                              if ' '.join(thm.name.split()[:2]) == t]
            leftmenu_data.append((t,
                                  t.replace(' ', ''),
                                  leftmenu_infos))
    else:
        # [(active_category_slug, themes_slugs, themes_links, themes_names)]
        leftmenu_data = [(active_category.slug,
                          thm.slug,
                          '/' + active_category.slug + '/' + thm.slug,
                          thm.name)
                         for thm in Theme.objects.filter(
                             category_id=category_object.id)
                         .order_by('order')]

    tiles_data = [(thm.slug,
                   [(tile.name, tile.content)
                    for tile in Tile.objects.filter(
                        theme_id=thm.id)
                    .order_by('order')])
                  for thm in Theme.objects.filter(
                      category_id=active_category.id)
                  .order_by('order')]

    news_data = []
    if active_category.slug == 'accueil':
        news_data = [('-'.join(str(o.date).split(sep='-')[::-1]),
                      o.title,
                      o.content)
                     for o in News.objects.all().order_by('date')][::-1]

    alternate_templates = {'accueil': 'home.html',
                           'calcul-mental': 'mental_calculation.html'}

    return render_to_response(alternate_templates.get(active_category.slug,
                                                      'default.html'),
                              {'navbar_data': navbar_data,
                               'leftmenu_data': leftmenu_data,
                               'active_category': active_category.name,
                               'category_content': active_category.text,
                               'category_slug': active_category.slug,
                               'tiles_data': tiles_data,
                               'footer': footer,
                               'footer_data': footer_data,
                               'news_data': news_data,
                               'test_var': leftmenu_data,
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
