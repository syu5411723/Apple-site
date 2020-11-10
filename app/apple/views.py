from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Device


class Index(TemplateView):
    template_name = 'index.html'


class DeviceTable(TemplateView):
    model = Device
    template_name = 'device_choice.html'

    def get_queryset(self):
        query = Device.objects.all()
        if 'query' in self.request.GET:
            qs = self.request.GET['query']
            query = query.filter(name__exact=qs)

        return query


class DeviceChoice(ListView):
    model = Device
    template_name = 'device_choice.html'


class Test(ListView):
    model = Device
    template_name = 'test.html'


