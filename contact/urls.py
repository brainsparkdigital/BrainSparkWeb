from django.urls import path
from .views import index, confirmation

urlpatterns = [
    path('contact/', index, name='contact'), # Main View Email send
    path('confirmed/', confirmation, name='confirmation'), # Just view an html contact submission
]
