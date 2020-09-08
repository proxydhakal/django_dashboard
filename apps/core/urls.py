from django.urls import path
from apps.core.views import index, dash_accounting,dash_desing, dash_engineering


urlpatterns = [
    path('', index, name='index'),
    path('<str:name>', dash_desing, name='design'),
    path('dash_engineering/', dash_engineering, name='engineering'),
    path('dash_accounting/', dash_accounting, name='accounting'),

]