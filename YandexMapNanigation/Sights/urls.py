from django.urls import path
from .views import SightsListView, SightDetailView, SightCreateView, SightDeleteView, SightUpdateView

app_name = 'sight'

urlpatterns = [
    path('', SightsListView.as_view(), name='list'),
    path('sights/<int:id>/', SightDetailView.as_view(), name='detail'),
    path('sight/create/', SightCreateView.as_view(), name='create'),
    path('sight/<int:id>/delete/', SightDeleteView.as_view(), name='delete'),
    path('sight/<int:id>/edit/', SightUpdateView.as_view(), name='edit')
]