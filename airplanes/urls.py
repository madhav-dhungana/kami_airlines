from django.urls import path
from .views import AeroplaneListCreateView, AeroplaneDetailView

urlpatterns = [
    path('airplanes/', AeroplaneListCreateView.as_view(), name='aeroplane-list-create'),
     path('airplanes/<int:pk>/', AeroplaneDetailView.as_view(), name='aeroplane-detail'),
]

