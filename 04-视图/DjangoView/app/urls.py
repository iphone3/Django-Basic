from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),


    # http://127.0.0.1:8000/detail/4/
    # detail/4/
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
]
