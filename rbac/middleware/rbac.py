#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from django.conf import settings
import re

class Check_Permission(MiddlewareMixin):
    def process_request(self,request):
        valid_url_list=settings.VALID_URL_LIST
        current_url=request.path_info
        permission_list=request.session.get(settings.PERMISSION_SESSION_KEY)
        for valid_url in valid_url_list:
            if re.match(valid_url,current_url):
                return None
        if not permission_list:
            return HttpResponse('用户未授权')
        flag=False
        for url in permission_list:
            reg='^%s$' % url
            if re.match(reg,current_url):
                flag=True
                break
        if not flag:
            return HttpResponse('无权访问')

