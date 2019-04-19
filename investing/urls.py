from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='investing-index'),
    path('api/', views.InvestmentList.as_view()),
    path('api/<int:pk>/', views.InvestmentDetail.as_view()),
]
