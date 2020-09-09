from django.urls import path
from apps.core.views import index, dashboardView


urlpatterns = [
    path('', index, name='index'),
    path('<str:name>', dashboardView, name='design'),
]