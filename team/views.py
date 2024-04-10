from django.shortcuts import render, redirect, get_object_or_404
from .models import Team
from .forms import TeamForm

# Create your views here.


def team(request):
    """ A view to return the team page """

    team_members = Team.objects.all()
    context = {
        'team_members': team_members
    }
    return render(request, 'team/team.html', context)


def add_team_member(request):
    """ A view to add a new member of staff """

    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team')
    
    form = TeamForm()
    context = {
        'form': form
    }
    return render(request, 'team/add_team_member.html', context)


def edit_team_member(request, member_id):
    team_member = get_object_or_404(Team, id=member_id)
    if request.method == "POST":
        form = TeamForm(request.POST, instance=team_member)
        if form.is_valid():
            form.save()
            return redirect('team')
    form = TeamForm(instance=team_member)
    context = {
        'form': form
    }
    return render(request, 'team/edit_team_member.html', context)