from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexCalculator.as_view(), name='index_calculator'),
]
