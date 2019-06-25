from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from mt.models import News


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


    # 新闻列表信息
    news_list = News.objects.all()

    # ifequal的使用
    active = 'index'

    # 过滤器
    temp_str = 'hello World!'
    import datetime
    now_time = datetime.datetime.now()


    # include
    shop_title1 = '家电'
    shop_list1 = ['电视', '空调', '洗衣机']
    shop_title2 = '手机'
    shop_list2 = ['苹果', '华为', 'OPPO']

    context = {
        'name': username,
        'age': age,
        'names':names,
        'user_list': user_list,
        'news_list':news_list,
        'active': active,
        'temp_str':temp_str,
        'now_time':now_time,
        'shop_title1':shop_title1,
        'shop_list1':shop_list1,
        'shop_title2':shop_title2,
        'shop_list2':shop_list2
    }

    return render(request, 'index.html', context=context)


def cart(request):

    return render(request, 'cart.html', context={'active':'cart'})


def mine(request):
    return render(request, 'mine.html', context={'active':'mine'})


def sort(request):
    return render(request, 'sort.html', context={'active':'sort'})


def setting(request):
    return render(request, 'setting.html', context={'active':'setting'})


def test(request):
    return render(request, 'test.html')


def test2(request):
    return render(request, 'test2.html')
