from django.urls import path
from app2.views import *

app_name='About'

urlpatterns=[path('About/',About,name='About'),

    ]