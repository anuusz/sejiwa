from django.urls import path
from . import views

urlpatterns = [
    path('', views.mental_health_test, name='mental_health_test'),
    path('../tes/', views.tes_view, name='tes'),
]