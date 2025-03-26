from django.urls import path
from . import views

urlpatterns = [
    path('', views.filesys, name='filesys'),  # Filesys main view
]