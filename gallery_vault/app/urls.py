from django.urls import path
from . import views

urlpatterns = [
    path('',views.gal_login),
    path('register',views.register),
    path('gal_home',views.gal_home),
    path('gal_logout',views.gal_logout),









#*********************USER*******************

    path('user_home',views.user_home),
    path('file_upd',views.file_upd),



]