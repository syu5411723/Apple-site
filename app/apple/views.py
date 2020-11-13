from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import DeviceModel
from django.http import HttpResponseNotAllowed


class Index(TemplateView):
    template_name = 'index.html'


def DeviceSearch(request):
    print("[request method]", request.method)
    if request.method == "POST":
        name1 = request.POST.get('phone_name_1')
        name2 = request.POST.get('phone_name_2')
        device_model_a = DeviceModel.objects.filter(name__exact=name1)
        device_model_b = DeviceModel.objects.filter(name__exact=name2)
        context = {
            'device_models': (device_model_a, device_model_b)
        }
    else:
        context = {'device_models': DeviceModel.objects.all()}
    return render(request, 'device_list.html', context)

















