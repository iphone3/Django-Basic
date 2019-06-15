from django.conf.urls import url
from app import views

urlpatterns = [
    url('^index/', views.index),
]
