from django.shortcuts import render

# garbage/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("これはトップページです。AIごみ判別アプリへようこそ。")