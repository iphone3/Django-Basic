from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):

    # 用户名
    username = 'root'
    age = 18

    context = {
        'name': username,
        'age': age,
    }

    return render(request, 'index.html', context=context)
