from django.db import models

# ORM 对象关系映射
# 定义模型
# 学生模型类
class Student(models.Model):
    # 名字
    name = models.CharField(max_length=100)
    # 成绩
    score = models.IntegerField()


# 商品模型类
class Goods(models.Model):
    # 主键
    g_id = models.AutoField(primary_key=True)
    # 名称
    g_name = models.CharField(max_length=255, default='')
    # 价格
    g_price = models.DecimalField(max_digits=10,decimal_places=2)
    # 是否删除 (逻辑删除)
    is_del = models.BooleanField(default=False)
    # 创建时间
    create_time = models.DateField(auto_now_add=True, null=True)
    # 修改时间
    change_time = models.DateTimeField(auto_now=True, null=True)
    # 测试字段
    img = models.CharField(null=True, max_length=100)
