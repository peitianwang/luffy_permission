#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
def init_permission(current_user,request):
    permission_queryset=current_user.roles.filter(permissions__isnull=False).values('permissions__id',
                                                                                    'permissions__url',
                                                                                    'permissions__title',
                                                                                    'permissions__menu__id',
                                                                                    'permissions__menu__icon',
                                                                                    'permissions__menu__title',
                                                                                    ).distinct()
    # for item in permission_queryset:
    #     print(item)
    print(permission_queryset)
    menu_dict={}
    permission_list=[]
    for item in permission_queryset:
        permission_list.append(permission_list.append(item['permissions__url']))

        menu_id=item['permissions__menu__id']
        if not menu_id:
            continue

        node={'title':item['permissions__title'], 'url':item['permissions__url']}

        if menu_id in menu_dict:
            menu_dict[menu_id]['children'].append(node)

        else:
            menu_dict[menu_id]={
                'title':item['permissions__menu__title'],
                'icon':item['permissions__menu__icon'],
                'children':[node,]
            }

    print(menu_dict.values())
    print('###############################')
    print(menu_dict.items())
    print('###############################')
    print(menu_dict)
    # for key,value in menu_dict:
    #     print(key,value)

    request.session[settings.PERMISSION_SESSION_KEY]=permission_list
    request.session[settings.MENU_SESSION_KEY]=menu_dict
    # permission_list=[item['permissions__url'] for item in permission_queryset]
    # request.session[settings.PERMISSION_SESSION_KEY]=permission_list