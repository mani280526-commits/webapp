from django.urls import path
from . import views

urlpatterns = [
    path('getemployeesapi/',views.GetEmpAPI.as_view()),
    path('modifyemployeeapi/<int:pk>/',views.ModifyEmpAPI.as_view()),
    path('custominsertapi/',views.CustomInsertAPI.as_view()),
    path('custommodifyapi/<int:pk>/',views.CustomModifyAPI.as_view()),
]