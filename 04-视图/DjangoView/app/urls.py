from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),


    # http://127.0.0.1:8000/detail/4/
    # detail/4/
    url(r'^detail/(\d+)/$', views.detail, name='detail'),

    # 3/1
    # 3/2
    # 3_1
    # 3_2
    url(r'^urlarg/(\d+)/(\d+)/(\w+)/$', views.urlarg, name='urlarg'),

    url(r'^goods_detail/(?P<type_name>\w+)/(?P<goods_id>\d+)/$', views.goods_detail, name='goods_detail'),
]
