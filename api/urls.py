from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('userss-list/', views.UserssList, name="userss-list"),
    path('userss-detail/<str:pk>/', views.UserssDetail, name="userss-detail"),
    path('userss-create/', views.UserssCreate, name="userss-create"),
    path('userss-update/<str:pk>/', views.UserssUpdate, name="userss-update"),
    path('userss-delete/<str:pk>/', views.UserssDelete, name="userss-delete")
]