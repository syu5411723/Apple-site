from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('device_list', views.DeviceSearch, name='device_list'),

]