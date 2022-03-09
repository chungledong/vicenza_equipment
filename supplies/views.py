from django.db.models import Q
from django.views import View
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .forms import SuppliesSearchForm
from .models import (
    GroupSupplies,
    Supplies,

)
# Create your views here.


def homeView(request):
    template_name = 'supplies/home.html'
    queryset = None
    form = SuppliesSearchForm(request.POST or None)
    print(request.method)

    context = {'name': "Xin chao Device",
               'form': form,
               'supplies': queryset,
               'groups': GroupSupplies.objects.all(),
               }

    if request.method == 'POST':
        text_input = request.POST.get('text_input')
        queryset = Supplies.objects.filter(
            Q(code__icontains=text_input) |
            Q(name__icontains=text_input)
        ).distinct()
        print(queryset)

        context = {'name': "Xin chao Device",
                   'form': form,
                   'supplies': queryset,
                   'groups': GroupSupplies.objects.all(),
                   }

    return render(request, template_name, context)


class SuppliesDetailView(DetailView):
    model = Supplies
    template_name = 'supplies/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Supplies.__name__
        return context


class GroupSuppliesListView(ListView):
    model = GroupSupplies
    template_name = 'supplies/groupsupplies-view.html'
    context_object_name = "groupsupplies"
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = GroupSupplies.__name__
        return context

    def get_queryset(self):
        return GroupSupplies.objects.filter(active=True)


class SuppliesListView(ListView):
    model = Supplies
    template_name = 'supplies/supplies-view.html'
    context_object_name = 'supplies'
    paginate_by = 6   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Supplies.__name__
        return context

    def get_queryset(self):
        return Supplies.objects.filter(active=True)


class SuppliesListViewByGroup(ListView):
    model = Supplies
    template_name = 'supplies/list-supplies.html'
    context_object_name = 'gsupplies'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Supplies.__name__
        return context

    def get_queryset(self):
        return Supplies.objects.filter(group_supplies=self.kwargs['pk'])
