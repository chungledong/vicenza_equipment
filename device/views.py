from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .forms import GroupDeviceForms, DeviceSearchForm
from .models import (
    GroupDevice,
    Device,
)
# Create your views here.


def homeView(request):
    template_name = 'device/home.html'
    context = {'name': "Xin chao Device",
               'form':DeviceSearchForm( request.POST or None)
               } 
       
    return render(request, template_name, context)

class GroupDeviceListView(ListView):
    model = GroupDevice
    template_name = 'device/groupdevices-view.html'
    context_object_name = 'groupdevices'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = GroupDevice.__name__        
        return context

    def get_queryset(self):
        return GroupDevice.objects.filter(active=True)


class DeviceListView(ListView):
    model = Device
    template_name = 'device/list-device.html'
    #context_object_name = 'device'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Device.__name__
        return context

    def get_queryset(self):
        return Device.objects.filter(group_device=self.kwargs['pk'])


class SuppliesOfDeviceListView(ListView):
    model = Device
    template_name = 'device/list-supplies-device.html'
    context_object_name = 'device'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        device = Device.objects.get(pk=self.kwargs['pk'])
        #context["device"] = device
        context["supplies"] = device.supplies.all()
        return context

    def get_queryset(self):
        return Device.objects.get(pk=self.kwargs['pk'])
