from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic import (ListView, DetailView, CreateView, 
                                  UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Ramen
from .forms import RamenForm


class HomePageView(TemplateView):
    template_name = 'ramen_rater/home.html'


class IndexView(ListView):
    queryset = Ramen.objects.order_by('-daterate')  
    context_object_name = 'ramen_list'
    template_name = 'ramen_rater/index.html'
    paginate_by = 10


class RamenDetails(DetailView):
    queryset = Ramen.objects.all()
    context_object_name = 'ramen'
    template_name = 'ramen_rater/detail.html'


class AddRamen(CreateView):
    model = Ramen
    form_class = RamenForm
    template_name = 'ramen_rater/add.html'


class EditRamen(UpdateView):
    model = Ramen
    form_class = RamenForm
    template_name = 'ramen_rater/edit.html'


class DeleteRamen(DeleteView):
    model = Ramen
    template_name = 'ramen_rater/delete.html'
    success_url = reverse_lazy('index')


class SearchRamen(ListView):
    template_name = 'ramen_rater/search.html'
    context_object_name = 'result'
    

    def get_queryset(self):
        query = self.request.GET['q']
        if query:
            return Ramen.objects.filter(Q(brand__icontains=query) |
                                        Q(variety__icontains=query) |
                                        Q(country__icontains=query) |
                                        Q(style__icontains=query)) 

        else:
            return Ramen.objects.all()

            











   
