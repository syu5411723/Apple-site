from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('choice', views.Choice.as_view(), name='choice'),
    path('detail', views.DeviceDetail.as_view(), name='detail'),
]