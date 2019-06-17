import random

from django.http import HttpResponse
from django.shortcuts import render
from app.models import Student


def index(request):
    return HttpResponse('hello Django！')


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
