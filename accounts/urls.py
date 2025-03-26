from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='accounts'),
    path('<str:account_name>/', include([
        path('filesys/', include('filesys.urls')),
        path('correspondence/', include('correspondence.urls')),
        path('reports/', include('reports.urls')),
    ])),
]