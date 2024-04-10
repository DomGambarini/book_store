from django.urls import path
from . import views

urlpatterns = [
    path('', views.team, name='team'),
    path('add_member/', views.add_team_member, name='add_team_member'),
    path('edit_member/<member_id>', views.edit_team_member, name='edit_team_member'),
    path('delete_member/<member_id>', views.delete_team_member, name='delete_team_member'),
]
