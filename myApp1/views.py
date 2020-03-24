from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt


class Hello(View):
    def get(self, request):
        return HttpResponse("hello GET ")
    def post(self,request):
        return HttpResponse("hello POST")
    def delete(self,request):
        return HttpResponse("hello DELETE")

def test(View):
    pass
    return "hello!!!!!!!!!!!!22222"