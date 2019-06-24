from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):

    # 用户名
    username = 'atom'
    age = 18

    return render(request, 'index.html', context={'name': username, 'age': age})
