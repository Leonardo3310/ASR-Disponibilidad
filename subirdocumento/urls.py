from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('subirdocumento/', views.alarm_list),
    path('subirdocumento/<int:variable_id>', views.generate_alarm),
]