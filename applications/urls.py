from django.urls import path
from . import views

urlpatterns = [
    path('apply/<uuid:rfp_id>/', views.apply, name='apply'),
]
