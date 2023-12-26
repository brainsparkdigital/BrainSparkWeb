#pages/urls
from django.urls import path
from .views import HomepageView, AboutPageView
# from . import views

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    # path('contact/', views.contact_view, name='contact'),
    # path('contact/success/', views.contact_success, name='contact_success'),
    path('', HomepageView.as_view(), name='home'),
]
