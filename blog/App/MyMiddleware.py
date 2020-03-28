from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.utils.deprecation import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):
    def process_request(self,request):
        if request.user.is_authenticated:
            return
        elif request.path == '/user/register/':
            return
        elif request.path !='/user/loginb/':
            return redirect('/user/loginb/')

