from django.shortcuts import render,HttpResponse,redirect
from rbac import models
from rbac.service.init_permission import init_permission

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request,'login.html',locals())
    user=request.POST.get('user')
    pwd=request.POST.get('pwd')
    current_user=models.UserInfo.objects.filter(name=user,password=pwd).first()
    if not current_user:
        return render(request,'login.html',{'msg':'用户不存在或账号密码错误'})
    # permission_list=current_user.roles.all().values('permissions__id','permissions__url').distinct()
    init_permission(current_user,request)
    return redirect('/customer/list/')
