from django.urls import path
from . import views

urlpatterns = [
    path('', views.team, name='team'),
    path('add_member/', views.add_team_member, name='add_team_member'),
]
