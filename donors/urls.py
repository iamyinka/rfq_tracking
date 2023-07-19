from django.urls import path
from . import views

urlpatterns = [
    path("add-donor/", views.add_donor, name="add-donor"),
]
