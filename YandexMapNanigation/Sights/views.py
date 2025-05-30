from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Sight
from .forms import SightForm


class SightsListView(ListView):
    model = Sight
    template_name = "index.html"
    paginate_by = 8


class SightDetailView(DetailView):
    model = Sight
    template_name = "sight_detail.html"
    pk_url_kwarg = "id"


class SightCreateView(LoginRequiredMixin, CreateView):
    model = Sight
    form_class = SightForm
    template_name = "sight_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('sight:list')
    

class SightUpdateView(LoginRequiredMixin, UpdateView):
    model = Sight
    form_class = SightForm
    template_name = 'sight_create.html'
    pk_url_kwarg = 'id'

    def dispatch(self, request, *args, **kwargs):
        sight = self.get_object()
        if sight.author != self.request.user:
            return redirect('sight:list')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('sight:list')


class SightDeleteView(LoginRequiredMixin, DeleteView):
    model = Sight
    template_name = 'sight_create.html'
    pk_url_kwarg = 'id'

    def dispatch(self, request, *args, **kwargs):
        sight = self.get_object()
        if sight.author != self.request.user:
            return redirect('sight:list')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('sight:list')