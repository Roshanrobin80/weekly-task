from django.urls import path
from .import views

urlpatterns = [
    path('',views.rrhome),
    path('rrhome',views.rrhome),
    path('contact',views.contact),
]       
