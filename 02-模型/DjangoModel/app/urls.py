from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^addstu/$', views.addStudent),
    url(r'^getstu/$', views.getStudents),
    url(r'^addgoods/$', views.addGoods),
    url(r'^changegoods/$', views.changegoods),
]
