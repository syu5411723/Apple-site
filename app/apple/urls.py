from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('device_choice', views.DeviceChoice.as_view(), name='device_choice'),
    path('device_table', views.DeviceTable.as_view(), name='device_table'),
    path('test', views.Test.as_view(), name='test'),
]