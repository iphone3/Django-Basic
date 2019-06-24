from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):

    # 用户名
    username = 'root'
    age = 18
    names = [
        '张三',
        '李四',
        '王五',
        '赵六',
        '田七'
    ]

    user_list = [
        {
            'username':'张三',
            'score': 98,
            'age': 18
        },
        {
            'username': '李四',
            'score': 78,
            'age': 32
        },
        {
            'username': '王五',
            'score': 91,
            'age': 13
        },
    ]


    context = {
        'name': username,
        'age': age,
        'names':names,
        'user_list': user_list
    }

    return render(request, 'index.html', context=context)
