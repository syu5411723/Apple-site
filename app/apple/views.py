from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Device


class Index(TemplateView):
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        device_list = Device.objects.all()
        context = {
            'device_list': device_list
        }
        return context


class DeviceDetail(DetailView):
    model = Device
    template_name = 'detail.html'


class Choice(TemplateView):
    template_name = 'choice.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        device_list = Device.objects.all()
        context = {
            'device_list': device_list
        }
        return context

