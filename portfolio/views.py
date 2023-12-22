# articles/views.py
from django.views.generic import ListView, DetailView

from .models import PortFolio

class PortfolioListView(ListView):
    model = PortFolio
    template_name = "portfolio.html"


class PortfolioDetailView(DetailView):
    model = PortFolio
    template_name = "portfolio_detail.html"