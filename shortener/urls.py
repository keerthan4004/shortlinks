from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('qr/<str:short_code>/', views.generate_qr, name='generate_qr'),
    path('<str:short_code>/', views.redirect_url, name='redirect_url'),
]