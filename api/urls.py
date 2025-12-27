from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import EmpRetrieveUpdateDeleteAPIView
from rest_framework.routers import DefaultRouter
from . import views

routes = DefaultRouter()
routes.register(r'employee',views.EmpViewSet,basename='employee')

urlpatterns = [
    path('getemployeesapi/',views.GetEmpAPI.as_view()),
    path('modifyemployeeapi/<int:pk>/',views.ModifyEmpAPI.as_view()),
    path('custominsertapi/',views.CustomInsertAPI.as_view()),
    path('custommodifyapi/<int:pk>/',views.CustomModifyAPI.as_view()),
    path('registeruserapi/',views.RegisterUserAPI.as_view()),
    path('loginapi/',TokenObtainPairView.as_view()),
    path('refreshapi/',TokenRefreshView.as_view()),
    path('searchapi/',views.SearchAPI.as_view()),
    path('getgenericapi/', views.EmpGenericAPIView.as_view()),
    path('employees/<int:pk>/', EmpRetrieveUpdateDeleteAPIView.as_view()),
    path('', include(routes.urls)),
]
