# articles/views.py
from django.views.generic import ListView, DetailView

from .models import Service

class ServiceListView(ListView):
    model = Service
    template_name = "services.html"


class ServiceDetailView(DetailView):
    model = Service
    template_name = "service_detail.html"