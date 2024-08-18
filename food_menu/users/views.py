from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') 
            form.save()
            messages.success(request, f"Welcome {username}, your account was created successfully!")
            return redirect('login') 
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def login(request):
    return render(request, 'login.html')
