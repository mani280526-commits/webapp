from django.urls import path
from . import views

urlpatterns = [
    path('getemployeesapi/',views.GetEmpAPI.as_view()),
]