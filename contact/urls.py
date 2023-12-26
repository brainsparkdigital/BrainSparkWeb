from django.urls import path
from .views import index, confirmation

urlpatterns = [
    path('contact/', index, name='contact'),
    path('confirmed/', confirmation, name='confirmed'),
]
