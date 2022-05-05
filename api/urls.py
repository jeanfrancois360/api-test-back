from django.urls import path
from . import views

urlpatterns = [
    path('', views.getMembers),
    path('add/', views.addMember),
    path('<str:pk>/update/', views.updateMember),
    path('<str:pk>/delete/', views.deleteMember),
    path('<str:pk>/', views.getMember),
]

