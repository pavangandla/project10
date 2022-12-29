from django.urls import path
from app2.views import *
app_name="something2"

urlpatterns=[
    path('youtube/',youtube,name='youtube'),
    path('naveen/',naveen,name='naveen'),
]