from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Event
from .forms import EventForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def events(request):
    """ A view to return the event page """

    events = Event.objects.all()
    context = {
        'events': events
    }

    return render(request, 'events/events.html', context)


@login_required
def add_event(request):
    """ A view to add a new event """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == "POST":
        # form = EventForm(request.POST)
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events')

    form = EventForm()
    context = {
        'form': form
    }
    return render(request, 'events/add_event.html', context)


@login_required
def edit_event(request, event_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events')
    form = EventForm(instance=event)
    context = {
        'form': form,
    }
    return render(request, 'events/edit_event.html', context)


@login_required
def delete_event(request, event_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('events')
