from django.shortcuts import render
from .models import Event
from .forms import EventForm

# Create your views here.

def events(request):
    """ A view to return the event page """

    events = Event.objects.all()
    context = {
        'events': events
    }

    return render(request, 'events/events.html', context)


def add_event(request):
    """ A view to add a new member of staff """

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events')
    
    form = EventForm()
    context = {
        'form': form
    }
    return render(request, 'events/add_event.html', context)


# def edit_team_member(request, member_id):
#     team_member = get_object_or_404(Team, id=member_id)
#     if request.method == "POST":
#         form = TeamForm(request.POST, instance=team_member)
#         if form.is_valid():
#             form.save()
#             return redirect('team')
#     form = TeamForm(instance=team_member)
#     context = {
#         'form': form
#     }
#     return render(request, 'team/edit_team_member.html', context)


# def delete_team_member(request, member_id):
#     team_member = get_object_or_404(Team, id=member_id)
#     team_member.delete()
#     return redirect('team')
