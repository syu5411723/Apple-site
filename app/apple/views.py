from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import DeviceModel


class Index(TemplateView):
    template_name = 'index.html'


class DeviceTable(TemplateView):
    model = DeviceModel
    template_name = 'device_detail.html'

    def get_queryset(self):
        queryset = DeviceModel.objects.all()
        if 'query' in self.request.GET:
            qs = self.request.GET['query']
            queryset = queryset.filter(name__exact=qs)

        return queryset


def DeviceSearch(request):
    if request.method == "POST":
        name = request.POST.get('name')
        device_name = DeviceModel.objects.filter(name__exact=name)
    return render(request, 'choice.html', device_name)


class Test(ListView):
    model = DeviceModel
    template_name = 'test.html'







