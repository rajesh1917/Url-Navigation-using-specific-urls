from django.urls import path
from app1.views import *

app_name='Home'

urlpatterns=[path('Home/',Home,name='Home'),

    ]