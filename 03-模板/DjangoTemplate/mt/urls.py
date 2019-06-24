from django.conf.urls import url

from mt import views

urlpatterns = [
    url(r'^$', views.index)
]

