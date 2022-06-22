from importlib.resources import contents
from json import load
from telnetlib import DO
from urllib import request
from django.shortcuts import render

def home(request):
    import json
    import requests

    if request.method == 'POST':
        ticker=request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" +ticker+ "/quote?token=pk_1ffa77ce7e4440e1b71d0bef0e6d0cea")
        try:
            api=json.loads(api_request.content)
        except Exception as e:
            api="Error......"
        return render(request, 'home.html' , {'api':api})



    else:
        return render(request, 'home.html' , {'ticker':"ENTER A TICKER SYMBOL ABOVE.........."})
    





def about(request):
    return render(request, 'about.html' , {})



def addstock(request):
    return render(request, 'addstock.html' , {})




