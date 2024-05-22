from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserForm
from .models import CustomUser

def user_list(request):
    """
    View to display a list of all users (if permitted).

    Requires appropriate permission checks for security.
    """
    users = CustomUser.objects.all()  # Fetch all users from your custom model
    context = {'users': users}
    return render(request, 'user_list.html', context)

def user_detail(request, pk):
    """
    View to display details of a specific user.

    Requires appropriate permission checks for security.
    """
    user = CustomUser.objects.get(pk=pk)  # Fetch user by primary key
    context = {'user': user}
    return render(request, 'user_detail.html', context)

def user_create(request):
    """
    View to create a new user.

    Handles form submission and user creation logic.
    """
    if request.method == 'POST':
        form = CustomUserForm(request.POST)  # Create form instance with POST data
        if form.is_valid():
            user = form.save()  # Save the new user
            # Additional processing after user creation (e.g., send welcome email)
            return redirect('user_list')  # Redirect to user list after successful creation
    else:
        form = CustomUserForm()  # Create empty form instance for GET requests
    context = {'form': form}
    return render(request, 'user_create.html', context)

def user_update(request, pk):
    """
    View to update an existing user.

    Handles form submission and user update logic.
    Requires appropriate permission checks for security.
    """
    user = CustomUser.objects.get(pk=pk)  # Fetch user by primary key
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)  # Pre-populate the form
        if form.is_valid():
            form.save()  # Save the updated user
            return redirect('user_detail', pk=user.pk)  # Redirect to updated user detail
    else:
        form = CustomUserForm(instance=user)  # Create form instance pre-populated with user data
    context = {'form': form}
    return render(request, 'user_update.html', context)

def user_delete(request, pk):
    """
    View to delete an existing user.

    Requires appropriate permission checks and confirmation for security.
    """
    user = CustomUser.objects.get(pk=pk)  # Fetch user by primary key
    if request.method == 'POST':
        user.delete()  # Delete the user
        return redirect('user_list')  # Redirect to user list after deletion
    context = {'user': user}
    return render(request, 'user_delete.html', context)

def user_login(request):
    """
    View to handle user login.

    Redirects to appropriate page after login or displays error message.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            # Redirect to appropriate page after successful login (e.g., user profile)
            return redirect('user_profile')
        else:
            # Display error message for invalid credentials
            context = {'error': 'Invalid username or password'}
            return render(request, 'user_login.html', context)
    context = {}
    return render(request, 'user_login.html', context)

def user_logout(request):
    """
    View to handle user logout.

    Redirects to appropriate page after logout.
    """
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to login page after logout
