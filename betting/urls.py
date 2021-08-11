from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create-bet/', views.create_bet, name = 'create-bet'),
    path('update-bet/<int:pk>/', views.update_bet, name = 'update-bet'),
    path('delete-bet/<int:pk>/', views.delete_bet, name = 'delete-bet'),
]