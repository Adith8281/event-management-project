from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomRegistrationForm, CustomLoginForm
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,logout
from django.contrib import messages
from django.contrib.auth.hashers import check_password

def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

           
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken.")
                return render(request, 'register.html', {'form': form})

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered.")
                return render(request, 'register.html', {'form': form})

          
            hashed_password = make_password(password)

            
            User.objects.create(username=username, email=email, password=hashed_password)
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
    else:
        form = CustomRegistrationForm()

    return render(request, 'register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                messages.error(request, "Invalid username or password.")
                return render(request, 'login.html', {'form': form})

           
            if user and check_password(password, user.password):
                request.session['user_id'] = user.id  
                messages.success(request, "Login successful!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')




def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def team(request):
    return render(request,'team.html')