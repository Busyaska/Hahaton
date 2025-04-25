from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import path, reverse_lazy
from .forms import CustomUserCreationForm


urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', CreateView.as_view(template_name='registration/registration.html',
                                         form_class=CustomUserCreationForm,
                                         success_url = reverse_lazy('sight:list')), name='registration')
]