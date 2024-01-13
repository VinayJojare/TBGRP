# wordpredictor/urls.py
from django.urls import path
from . import views

app_name = 'wordpredictor'

urlpatterns = [
    path('', views.enter_sentence, name='enter_sentence'),
    path('capture_sentence/', views.capture_sentence, name='capture_sentence'),
    # Add other URL patterns as needed
]
