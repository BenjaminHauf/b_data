from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='accounts'),  # Overview page
    path('<str:account_name>/', include([
        path('filesys/', include('filesys.urls')),  # Account-specific filesystem
        path('correspondence/', include('correspondence.urls')),  # Account-specific correspondence
        path('reports/', include('reports.urls')),  # Account-specific reports
    ])),
]