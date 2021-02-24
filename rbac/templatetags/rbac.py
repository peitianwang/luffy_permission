#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.template import Library
from django.conf import settings
register=Library()

@register.inclusion_tag('rbac/static_menu.html')
def static_menu(request):
    menu_list=request.session.get(settings.MENU_SESSION_KEY)
    return {'menu_list':menu_list}

@register.inclusion_tag('rbac/multi_menu.html')
def multi_menu(request):
    menu_dict=request.session.get(settings.MENU_SESSION_KEY)
    return {'menu_dict':menu_dict}