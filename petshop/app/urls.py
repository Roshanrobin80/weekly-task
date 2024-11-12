from django.urls import path
from . import views

urlpatterns = [
    path('',views.shop_login),
    path('main_logout',views.main_logout),


    # --------------seller------------------

    path('shop_home',views.shop_home),
    path('add_pet',views.add_pet),
    # path('edit_pet/<pid>',views.edit_pet),
    # path('dlt_pet/<pid>',views.dlt_pet),


]