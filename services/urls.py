# articles/urls.py
from django.urls import path

from .views import ServiceListView, ServiceDetailView

urlpatterns = [
    path("services/<int:pk>", ServiceDetailView.as_view(), name="service_detail"),
    path("services/", ServiceListView.as_view(), name="services"),
]