from django.urls import path
from .views import PortfolioListView, PortfolioDetailView

urlpatterns = [
    path("portfolio/<slug:slug>", PortfolioDetailView.as_view(), name="portfolio_detail"),
    path("portfolio/", PortfolioListView.as_view(), name="portfolio"),
]
