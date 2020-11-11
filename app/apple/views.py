from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import DeviceModel
from django.http import HttpResponseNotAllowed


class Index(TemplateView):
    template_name = 'index.html'


class DeviceList(ListView):
    model = DeviceModel
    template_name = 'device_list.html'

    def DeviceSearch(request):
        if request.method != 'POST':
            return HttpResponseNotAllowed(['POST'])
        name = request.POST.get('name')
        device_name = DeviceModel.objects.filter(name__exact=name)
        return render(request, 'device_list.html', {'device_name': device_name})


class Test(TemplateView):
    model = DeviceModel
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        device_list = DeviceModel.objects.all()
        context = {
            'device_list': device_list
        }
        return context




