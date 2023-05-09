from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Url

# Create your views here.
import random

def index(response):
    if response.method == "POST":
        shortened = shorten_url(response.POST["url"])
        Url(id =shortened.split('/')[-1] ,link=add_https(response.POST["url"]),shortened=shortened).save()
        return render(response,'main/index.html',{'hidden' : False,'shortened':shortened})
        
    else:
        return render(response,'main/index.html',{'hidden' : True,'shortened':''})


def redirect_url(response,id):
    item = Url.objects.get(id=id)
    
    
    return redirect(item.link)
    

def shorten_url(url, base_url= "http://127.0.0.1:8000/"):
    return base_url+str(random.randint(0,100000000))

def add_https(url:str):
    if url.startswith("https") or url.startswith("http"):
        return url
    else:
        if url.startswith("www."):
            return "https://"+url
        else:
            return "https://www."+url
            
