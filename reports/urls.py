from django.urls import path
from . import views

urlpatterns = [
    path('', views.reports, name='reports'),  # Reports main view
]