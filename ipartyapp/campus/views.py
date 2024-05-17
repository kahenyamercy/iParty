from django.shortcuts import render, redirect
from .models import Campus
from .forms import CampusForm

def campus_list(request):
    campuses = Campus.objects.all()
    return render(request, 'campus_list.html', {'campuses': campuses})

def campus_detail(request, pk):
    campus = Campus.objects.get(pk=pk)
    return render(request, 'campus_detail.html', {'campus': campus})

def campus_create(request):
    if request.method == 'POST':
        form = CampusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campus_list')
    else:
        form = CampusForm()
    return render(request, 'campus_form.html', {'form': form})

def campus_update(request, pk):
    campus = Campus.objects.get(pk=pk)
    if request.method == 'POST':
        form = CampusForm(request.POST, instance=campus)
        if form.is_valid():
            form.save()
            return redirect('campus_list')
    else:
        form = CampusForm(instance=campus)
    return render(request, 'campus_form.html', {'form': form})

def campus_delete(request, pk):
    campus = Campus.objects.get(pk=pk)
    if request.method == 'POST':
        campus.delete()
        return redirect('campus_list')
    return render(request, 'campus_confirm_delete.html', {'campus': campus})
