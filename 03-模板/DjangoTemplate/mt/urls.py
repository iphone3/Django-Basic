from django.conf.urls import url

from mt import views

urlpatterns = [
    url(r'^$', views.index, name='index'),    # 首页
    url(r'^cartcartcart/$', views.cart, name='cart'),    # 购物车
    url(r'^mine/$', views.mine, name='mine'),    # 我的
    url(r'^sort/$', views.sort, name='sort'),    # 分类
    url(r'^setting/$', views.setting, name='setting'),    # 设置
    url(r'^test/$', views.test, name='test'),   # 继承测试
    url(r'^test2/$', views.test2, name='test2'),   # 继承测试
]

