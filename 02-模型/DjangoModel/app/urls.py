from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^addstu/$', views.addStudent),
    url(r'^getstu/$', views.getStudents),
    url(r'^addgoods/$', views.addGoods),
    url(r'^changegoods/$', views.changegoods),
    url(r'^showgoods/$', views.showgoods),
    url(r'^getgoods/$', views.getgoods),
    url(r'^aggregatetest/$', views.aggregatetest),
    url(r'^qtest/$', views.qtest),
    url(r'^ftest/$', views.ftest),
    url(r'^delgoods/$', views.delgoods),
]
