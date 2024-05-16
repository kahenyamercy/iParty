from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event

class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = 'event_form.html'
    fields = ['name', 'date', 'time', 'location', 'max_attendees', 'contribution_amount', 'campus']

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    template_name = 'event_form.html'
    fields = ['name', 'date', 'time', 'location', 'max_attendees', 'contribution_amount', 'campus']

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'event_confirm_delete.html'
    success_url = '/events/'
