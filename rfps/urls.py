from django.urls import path
from . import views

urlpatterns = [
    path('new/<str:donor_id>/', views.create_rfp, name='create-rfp'),
]