from django.urls import path
from . import views

app_name = "pages"  

urlpatterns = [
    path("", views.car_list, name="car_list"),
]
