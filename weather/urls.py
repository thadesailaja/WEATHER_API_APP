from django.urls import path
from weather.views import *
urlpatterns=[
    path('home/',home,name='home'),
]