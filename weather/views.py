from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from django.contrib import messages
import requests
import datetime
# Create your views here.

def home(request):
    if request.method=='POST':
        city=request.POST['city']
    else:
        city='indore'
    API='487c7ca8c6cd26995c4fdb7f5dc12f5d'
    url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}'
    AWD={'units':'metric'}
    #response=requests.get(url,AWD)
    #weather_data=response.json()
    try:
        data=requests.get(url,AWD).json()
        print(data)
        description=data['weather'][0]['description']
        icon=data['weather'][0]['icon']
        temp=data['main']['temp']
        humidity=data['main']['humidity']
        speed=data['wind']['speed']
        day=datetime.date.today()
        exception_occured=False
        dic={'city':city,'description':description,'icon':icon,'temp':temp,'humidity':humidity,'speed':speed,'day':day,'exception_occured':exception_occured}
        return render(request,'home.html',dic)
    
    except KeyError:
        exception_occured=True
        messages.error(request,'Entered data is not available to API')
        day=datetime.date.today()
        dic={'city':'indore','description':'Clear Sky','icon':'01d','temp':25,'day':day,'exception_occured':exception_occured}
        return render(request,'home.html',dic)