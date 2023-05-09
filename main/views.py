from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(response):
    if response.method == "POST":
        print(response.POST["url"])
        return render(response,'main/index.html',{'hidden' : False,'shortened':'https://www.google.com/'})
        
        
    # return HttpResponse("<h1>Trimly</h1>")
    else:
        return render(response,'main/index.html',{'hidden' : True,'shortened':''})