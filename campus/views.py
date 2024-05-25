from django.shortcuts import render, redirect, get_object_or_404
from .models import Campus
from .forms import CampusForm

def campus_list(request):
    campuses = Campus.objects.all()
    context = {'campuses': campuses}
    return render(request, 'campus_list.html', context)

def campus_detail(request, pk):
    campus = get_object_or_404(Campus, pk=pk)
    context = {'campus': campus}
    return render(request, 'campus_detail.html', context)

def campus_create(request):
    if request.method == 'POST':
        form = CampusForm(request.POST)  # Use the form to validate and save data
        if form.is_valid():
            form.save()
            return redirect('campus_list')
    else:
        form = CampusForm()
    context = {'form': form}
    return render(request, 'campus_create.html', context)

def campus_update(request, pk):
    campus = get_object_or_404(Campus, pk=pk)
    if request.method == 'POST':
        form = CampusForm(request.POST, instance=campus)  # Update existing campus
        if form.is_valid():
            form.save()
            return redirect('campus_detail', pk=pk)
    else:
        form = CampusForm(instance=campus)  # Pre-populate form with existing data
    context = {'form': form, 'campus': campus}
    return render(request, 'campus_update.html', context)

def campus_delete(request, pk):
    campus = get_object_or_404(Campus, pk=pk)
    if request.method == 'POST':
        campus.delete()
        return redirect('campus_list')
    context = {'campus': campus}
    return render(request, 'campus_delete.html', context)
