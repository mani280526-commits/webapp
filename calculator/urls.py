from django.urls import path
from . import views
urlpatterns=[
    path('',views.calculator),
    path('addition/',views.addition),
    path('mtable/',views.generatetable),
]