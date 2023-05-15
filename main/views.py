from django.forms import URLField
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Url
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

# Create your views here.
import random

def index(response):
    if response.method == "POST":      
          if validate_url(response.POST["url"])== True:
            shortened = shorten_url(response.POST["url"])
            Url(id =shortened.split('/')[-1] ,link=add_https(response.POST["url"]),shortened=shortened).save()
            return render(response,'main/index.html',{'hidden' : False,'shortened':shortened})
          else:
              return render(response,'main/index.html',{'hidden_error' : False,'shortened':""})
    else:
         return render(response,'main/index.html',{'hidden' : True,'shortened':''})

def redirect_url(response,id):
    item = Url.objects.get(id=id)
    return redirect(item.link) 
    
def shorten_url(url, base_url="www.trimly.info/"):
    while True:
        rand_num = random.randint(0, 1_000_000)
        if Url.objects.filter(id=rand_num).exists():
            continue
        break
    return base_url+str(rand_num)

def add_https(url:str):
    if url.startswith("https") or url.startswith("http"):
        return url
    else:
        if url.startswith("www."):
            return "https://"+url
        else:
            return "https://www."+url
        
def validate_url(url):
    url_form_field = URLField()
    try:
        url = url_form_field.clean(url)
    except ValidationError:
        return False
    return True