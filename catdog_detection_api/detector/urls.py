from django.urls import path
from . import views

urlpatterns = [
    path('', views.detect_request),
    path('api_request/', views.object_detection_api),
    #path('welcome/', views.welcome),
    #path('detect/', views.detect),
]