from django.urls import path
from . import views

urlpatterns = [
    path('addition/',views.Calculator.as_view()),
    path('multi/',views.Calculator2.as_view()),

]