from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('device_list', views.DeviceList.as_view(), name='device_list'),

    path('test', views.Test.as_view(), name='test'),
]