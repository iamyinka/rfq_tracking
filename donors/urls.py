from django.urls import path
from . import views

urlpatterns = [
    path("add-donor/", views.add_donor, name="add-donor"),
    path('donor-detail/<uuid:donor_id>/', views.donor_detail, name="donor-detail"),
]
