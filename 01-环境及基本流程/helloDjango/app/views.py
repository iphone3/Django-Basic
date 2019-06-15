from django.http import HttpResponse
from django.shortcuts import render

# 视图函数
def index(request):
    return HttpResponse('hello Django -- zyz')
