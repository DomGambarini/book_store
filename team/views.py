from django.shortcuts import render
from .models import Team

# Create your views here.


def team(request):
    """ A view to return the team page """

    team_members = Team.objects.all()
    context = {
        'team_members': team_members
    }
    return render(request, 'team/team.html', context)

