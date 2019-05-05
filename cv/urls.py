from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cv-index'),
    path('education/', views.education, name='cv-education')
]
