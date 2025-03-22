from django.urls import path
from .views import sample  # Import the view function

urlpatterns = [
    path('sample/', sample, name='sample'),
]
