# import os

# import yaml
from django.shortcuts import render_to_response
# from django.http import HttpResponse
# from django.conf import settings

from pages.models import Category, Theme

# CUR_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".")) + "/"
# with open(CUR_DIR + 'menus.yaml', mode='rt', encoding='utf8') as filepath:
#    MENUS = yaml.load(filepath)


def home(request):
    return category(request, category='Accueil')

def category(request, **kwargs):
    # todo: check the category does exist
    cat = kwargs.get('category', None)
    # todo: check a result at least is returned
    active_category = Category.objects.filter(name__exact=cat)[0]
    navbar_entries = [o.name for o in Category.objects.all().order_by('order')]
    leftmenu_entries = [o.name for o in Theme.objects.filter(category_id=active_category.id).order_by('order')] 
    return render_to_response('layout.html',
                              {'navbar_entries': navbar_entries,
                               'leftmenu_entries': leftmenu_entries,
                               'active': cat,
                               'content': active_category.text,
                               'test_var': 'rien à tester',
                               })

def theme(request, **kwargs):
    pass
