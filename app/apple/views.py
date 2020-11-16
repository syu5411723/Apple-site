from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import DeviceModel
from django.http import HttpResponseNotAllowed


class Index(TemplateView):
    template_name = 'index.html'


def DeviceSearch(request):
    print("[request method]", request.method)
    type_names = DeviceModel.objects.all().values_list('name', flat=True)
    if request.method == "POST":
        name1 = request.POST.get('name1')
        name2 = request.POST.get('name2')
        device_model_a = DeviceModel.objects.filter(name__exact=name1).first()
        device_model_b = DeviceModel.objects.filter(name__exact=name2).first()
        context = {
            'device_models': [device_model_a, device_model_b],
            'type_names': type_names
        }
        return render(request, 'device_list.html', context)
    else:
        context = {'type_names': type_names}
        return render(request, 'device_list.html', context)



















