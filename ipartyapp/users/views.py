from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomAuthenticationForm, CustomUserCreationForm

def register_user(request):
    """user registration"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.campus = form.cleaned_data['campus']
            user.phone_number = form.cleaned_data['phone_number']
            user_type = form.cleaned_data['user_type']
            if user_type == 'organizer':
                user.is_organizer = True
            else:
                user.is_attendee = True
            user.save()
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Form submission is invalid.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
        messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')
