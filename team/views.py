from django.shortcuts import render
from .models import Team

# Create your views here.


def team(request):
    """ A view to return the team page """

    team_member = Team.objects.all(
        context = {
            'team_member': team_member
        }
    )
    return render(request, 'team/team.html', context)

