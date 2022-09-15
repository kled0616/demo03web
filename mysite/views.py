from django.http import HttpResponse
from django.shortcuts import render
import datetime
# from .models import TodoList, Item

# # Create your views here.
# def index(response ,id ):
#     ls = TodoList.objects 
#     items = ls.items_set.get(id = id)
#     return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name,str(items.text)))


def home(request):
    # return "<h1>Home</h1>"
    # return HttpResponse("<h1>Home</h1>")
    now = datetime.datetime.now() # 現在時間
    context1 = {'now':now}  
    get_client_ip(request)  
    return render(request,"09/index.html",{})

# # Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print("--------------------------->" + ip)
