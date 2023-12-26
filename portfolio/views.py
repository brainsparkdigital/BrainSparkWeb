from django.views.generic import ListView, DetailView
from .models import Portfolio

class PortfolioListView(ListView):
    model = Portfolio
    template_name = "portfolio.html"

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = "portfolio_detail.html"
    slug_field = 'slug'  # Specify the slug field for the view

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio = self.object  # Access the object attribute directly
        images = portfolio.images.all()
        context['images'] = images
        return context
