from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from django.contrib import messages

@login_required
def event_list(request):
    events = Event.objects.all().order_by('-created_at')  # Order by recent first
    context = {'events': events}
    return render(request, 'event_list.html', context)

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)  # Include uploaded files
        if form.is_valid():
            event = form.save(commit=False)  # Don't save yet (set creator)
            event.created_by = request.user
            event.save()
            messages.success(request, 'Event created successfully!')
            return redirect('event_list')  # Redirect to event list
    else:
        form = EventForm()
    context = {'form': form}
    return render(request, 'event_create.html', context)

@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {'event': event}
    return render(request, 'event_detail.html', context)

@login_required
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)  # Update existing event
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_detail', pk=pk)  # Redirect to updated event detail
    else:
        form = EventForm(instance=event)  # Pre-populate form with existing data
    context = {'form': form, 'event': event}
    return render(request, 'event_update.html', context)

@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('event_list')  # Redirect to event list after deletion
    context = {'event': event}
    return render(request, 'event_delete.html', context)

@login_required
def register_for_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user not in event.attendees.all():
        event.attendees.add(request.user)  # Add user to event attendees
        messages.success(request, 'You are now registered for the event!')
    else:
        messages.warning(request, 'You are already registered for this event.')
    return redirect('event_detail', pk=pk)  # Redirect back to event detail
