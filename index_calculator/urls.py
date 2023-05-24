from django.urls import path
from . import views


urlpatterns = [
    #path('proba/', views.result, name='result'),
    #path('index-calc/', views.index_calc, name='index-calc'),
    # path('', views.IndexCalculator.as_view(), name='ic'),
    path('', views.IndexCalculator.as_view(), name='index_calculator'),
    # path('', views.result, name='result'),
]
