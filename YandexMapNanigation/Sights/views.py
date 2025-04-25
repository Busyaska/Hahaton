from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Sight
from .forms import SightForm


class SightsListView(ListView):
    model = Sight
    template_name = "index.html"
    paginate_by = 10


class SightDetailView(DetailView):
    model = Sight
    template_name = "sight_detail.html"
    pk_url_kwarg = "id"


class SightCreateView(CreateView):
    model = Sight
    form_class = SightForm
    template_name = "sight_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('sight:list')
