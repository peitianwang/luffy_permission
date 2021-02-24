from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def customer_list(request):
    return render(request,'customer_list.html',locals())
