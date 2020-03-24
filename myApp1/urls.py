from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include




from myApp1 import views
from myDjango2 import settings

app_name = "myApp1"
urlpatterns = [
    url(r'hello/', views.Hello.as_view(), name="hello"),
]

