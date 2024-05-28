from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserUpdateForm

@login_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

@login_required
def user_detail(request, pk):
    user = CustomUser.objects.get(pk=pk)
    return render(request, 'user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'User created successfully!')
                return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password!')
    return render(request, 'login.html')

@login_required
def user_update(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully!')
            return redirect('user_detail', pk=pk)
    else:
        form = CustomUserUpdateForm(instance=user)
    return render(request, 'user_update.html', {'form': form})

@login_required
def user_delete(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully!')
        return redirect('home')
    return render(request, 'user_delete.html', {'user': user})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout
