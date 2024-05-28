from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from events.models import Event

def landing_page(request):
    return render(request, 'index.html')


@login_required(login_url='/users/login/')
def dashboard(request):
    events = Event.objects.order_by('-date')[:10]
    return render(request, 'dashboard.html', {'events': events})
