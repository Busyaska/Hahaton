from django.urls import path
from .views import SightsListView, SightDetailView, SightCreateView

app_name = 'sight'

urlpatterns = [
    path('', SightsListView.as_view(), name='list'),
    path('sights/<int:id>/', SightDetailView.as_view(), name='detail'),
    path('sight/create/', SightCreateView.as_view(), name='create')
]