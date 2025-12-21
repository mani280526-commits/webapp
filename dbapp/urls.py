from django.urls import path
from . import views
urlpatterns=[
    path('',views.dbprocessing),
    path('insert/',views.insertemployee,name='inserturl'),
    path('select/',views.selectemployee, name='selecturl'),
    path('update/<int:eno>/',views.updateemployee,name='updateurl'),
    path('delect/<int:eno>/',views.deleteemployee,name='delecturl'),
]