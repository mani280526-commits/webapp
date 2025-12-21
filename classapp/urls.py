from django.urls import path
from . import views

urlpatterns = [
    path('addition/',views.Calculator.as_view()),
    path('multi/',views.Calculator2.as_view()),
    path('select/',views.SelectEmployee.as_view()),
    path('insert/',views.InsertEmployee.as_view()),
    path('update/<int:pk>/',views.ModifybEmployee.as_view()),
]