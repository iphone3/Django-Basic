from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def detail(request, goodsId):
    return HttpResponse('商品详情:' + goodsId)


def urlarg(request, a, b, c):
    return HttpResponse('a={}  b={}  c={}'.format(a,b,c))



def goods_detail(request, goods_id, type_name):
    return HttpResponse(' {} 分类 商品详情: {}'.format(type_name, goods_id))
