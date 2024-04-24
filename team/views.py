from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import Team
from .forms import TeamForm
from django.contrib.auth.decorators import login_required


def team(request):
    """ A view to return the team page """

    team_members = Team.objects.all()
    context = {
        'team_members': team_members
    }
    return render(request, 'team/team.html', context)


@login_required
def add_team_member(request):
    """ A view to add a new member of staff """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    template = 'team/add_team_member.html'

    if request.method == "POST":
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a new Team Member!')
            return redirect('team')
        else:
            messages.error(
                request,
                'Failed to add a team member. Please ensure the form is valid.'
                )
    else:
        form = TeamForm()

    template = 'team/add_team_member.html'
    context = {
        'form': form
        }
    return render(request, template, context)


@login_required
def edit_team_member(request, member_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    team_member = get_object_or_404(Team, id=member_id)
    if request.method == "POST":
        form = TeamForm(request.POST, request.FILES, instance=team_member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated team member!')
            return redirect('team')
        else:
            messages.error(
                request,
                'Failed to update. Please ensure the form is valid.')
    else:
        form = TeamForm(instance=team_member)
        messages.info(request, f'You are editing {team_member.name}')

    template = 'team/edit_team_member.html'
    context = {
        'form': form,
        'team': team,
    }
    return render(request, template, context)


@login_required
def delete_team_member(request, member_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    team_member = get_object_or_404(Team, id=member_id)
    team_member.delete()
    return redirect('team')
