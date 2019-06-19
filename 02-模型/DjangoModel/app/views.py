import random

from django.db.models import F
from django.db.models import Max, Min, Avg
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from app.models import Student, Goods, GoodsManager


def index(request):
    return render(request, template_name='index.html')


# 添加学生
def addStudent(request):

    # 实例化对象
    stu = Student()
    stu.name = str(random.randrange(1, 100)) + '-张三'
    stu.score = random.randrange(1, 100)

    # 存储到数据库
    stu.save()

    return HttpResponse('添加学生成功:' + stu.name)


# 获取学生信息
def getStudents(request):
    # 获取
    students = Student.objects.all()

    temp = ''
    for stu in students:
        # <p> </p>
        temp += ('<p>' + '名字:' + stu.name + '-' + '成绩:' + str(stu.score) + '</p>')

    return HttpResponse(temp)


# 添加商品
def addGoods(request):
    goods = Goods()
    goods.g_name = 'iphone-' + str(random.randrange(1,20))
    goods.g_price = random.randrange(9999,20000)
    goods.save()

    return HttpResponse('添加商品成功: ' + goods.g_name)

# 删除商品
def delgoods(request):
    goods = Goods.objects.first()
    goods.delete()

    return HttpResponse('删除数据成功')

# 修改商品
def changegoods(request):
    # 查询
    goods = Goods.objects.first()

    # 修改
    goods.g_name = 'iphone X'

    # 保存
    goods.save()

    return HttpResponse('修改商品成功')


# 结果集
def showgoods(request):

    # all()
    # goods_list = Goods.objects.all() # 将已经删除的排除
    # goods_list = Goods.objects.filter(is_del=False)

    goods_list = Goods.goodsObjects.all()
    # goods_list = Goods.objects.all()


    # filter() 符合要求的
    # goods_list = Goods.objects.filter(g_id=3)
    # goods_list = Goods.objects.filter(g_id__lt=3)
    # goods_list = Goods.objects.filter(g_id__lte=3)
    # goods_list = Goods.objects.filter(g_id__gt=3)
    # goods_list = Goods.objects.filter(g_id__gte=3)
    # goods_list = Goods.objects.filter(g_id__gt=3, g_price__gt=10)

    # exclude() 过滤掉符合要求的
    # goods_list = Goods.objects.exclude(g_price=11571)

    # 模糊查询
    # goods_list = Goods.objects.filter(g_name__startswith='k')
    # goods_list = Goods.objects.filter(g_name__endswith='8')
    # goods_list = Goods.objects.filter(g_name__contains='8')

    # 排序
    # goods_list = Goods.objects.order_by('g_price')  # 升序
    # goods_list = Goods.objects.order_by('-g_price')  # 升序

    # 包含
    # goods_list = Goods.objects.filter(g_id__in=[3,5,7,10])

    # 切片
    # goods_list = Goods.objects.order_by('g_price')[0:3]

    temp = ''
    for goods in goods_list:
        temp += '<p> {}-{} ￥{} </p>'.format(goods.g_id, goods.g_name, goods.g_price)

    return HttpResponse(temp)


# 单个
def getgoods(request):
    # goods = Goods.objects.first()

    # get
    # goods = Goods.objects.get(g_id=6)
    # goods = Goods.objects.get(g_price=10.11)    # 多个有问题
    # goods = Goods.objects.get(g_id=100) # 不存在

    goods_list = Goods.objects.filter(g_id=10)
    # if goods_list.count():
    #     goods = goods_list.first()

    if goods_list.exists():
        goods = goods_list.first()


    return HttpResponse('<p> {}-{} ￥{} </p>'.format(goods.g_id, goods.g_name, goods.g_price))


# 聚合函数
def aggregatetest(request):
    # Max() Min() Avg() ...

    # 获取最大值
    # maxDir = Goods.objects.aggregate(Max('g_price'))
    # 根据最大值，获取对应的商品对象
    # goods = Goods.objects.filter( g_price=maxDir['g_price__max']).first()

    # 获取最小值
    minDir = Goods.objects.aggregate(Min('g_price'))
    # 根据最小值，获取对应的商品对象
    # goods = Goods.objects.filter(g_price=Min['g_price__min']).first()

    # return HttpResponse('<p> {}-{} ￥{} </p>'.format(goods.g_id, goods.g_name, goods.g_price))

    # 平均价格
    # 获取最大值
    avgDir = Goods.objects.aggregate(Avg('g_price'))

    return HttpResponse('平均价格:' + str(avgDir['g_price__avg']))


# Q对象
def qtest(request):

    # 与 &
    # 或 |
    # 非 ~

    # id>5 且 价格>10
    # goods_list = Goods.objects.filter(g_id__gt=5).filter(g_price__gt=10)

    # 条件1: g_id__gt=5
    # 条件2: g_price__gt=10
    # goods_list = Goods.objects.filter( Q(g_id__gt=5) & Q(g_price__gt=10) )


    # id<3 或 价格>100
    # 条件1: g_id__lt=3
    # 条件2: g_price__gt=100
    # goods_list = Goods.objects.filter(Q(g_id__lt=3) | Q(g_price__gt=100))


    # id > 5
    # goods_list = Goods.objects.filter(g_id__gt=5)
    goods_list = Goods.objects.filter(~Q(g_id__lt=5))

    temp = ''
    for goods in goods_list:
        temp += '<p> {}-{} ￥{} </p>'.format(goods.g_id, goods.g_name, goods.g_price)

    return HttpResponse(temp)


# F对象
# 数学成绩 > 英语成绩  【自己和自己比较】
def ftest(request):

    students = Student.objects.filter(math__gt=F('english'))

    temp = ''
    for stu in students:
        # <p> </p>
        temp += ('<p>' + '名字:' + stu.name + '-' + '数学成绩:' + str(stu.math) + '英语成绩:' + str(stu.english) + '</p>')

    return HttpResponse(temp)

