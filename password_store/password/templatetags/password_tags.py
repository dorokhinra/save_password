from django import template
from django.db.models import Count

from password.models import *

register = template.Library()

menu = [{'name': 'Настройки', 'url': 'setting_pass'},
        {'name': 'Реестр', 'url': 'pass_reestr'},
        {'name': 'Создание и редактирование',
         'url': 'edit_reestr'}]


@register.inclusion_tag('password/list_menu.html', name='list_menu')
def show_menu(request=None, user=None):
    return {'menu': menu, 'request': request, 'user': user}


@register.inclusion_tag('password/list_footer.html', name='list_footer')
def show_footer(sorted=None, user=None):
    return {'menu': menu}


@register.inclusion_tag('password/modal.html', name='modal')
def show_modal():
    pass