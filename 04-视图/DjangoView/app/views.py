from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):

    return render(request, 'index.html')


def detail(request, goodsId):
    return HttpResponse('商品详情:' + goodsId)


def urlarg(request, a, b, c):
    return HttpResponse('a={}  b={}  c={}'.format(a,b,c))



def goods_detail(request, goods_id, type_name):
    return HttpResponse(' {} 分类 商品详情: {}'.format(type_name, goods_id))


def login_html(request):
    return render(request, 'login.html')


def login(request):
    # 登录成功后，重定向到首页
    # return redirect('/')
    return redirect('app:index')
    # return redirect('app:urlarg', 1,5,10)
    # return redirect('app:goods_detail', goods_id=10, type_name='服装类')
