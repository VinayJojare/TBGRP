# plagiarism_detector_app/urls.py
from django.urls import path
from .views import plagiarism_detect, result


urlpatterns = [
    path('', plagiarism_detect, name='plagiarism_detect'),
    path('result/<int:pk>/', result, name='result'),
    
]
