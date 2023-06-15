from django.shortcuts import render, redirect
from .models import *
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def register(request):
    return render(request, 'record/register.html')

def index(request):
    clients = Client.objects.all()
    employees = Employee.objects.all()
    posts = Posn.objects.all()
    services = Service.objects.all()
    records = Record.objects.all()
    locations = Location.objects.all()
    context = {
            'clients':clients,
            'employees':employees,
            'posts':posts,
            'services':services,
            'records':records,
            'locations':locations
            }
    return render(request, "record/index.html", context)

def sign_in(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')
        
        form = LoginForm()
        return render(request,'record/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,email=email,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {email}, welcome back!')
                return redirect('index')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'record/login.html',{'form': form})
    
def sign_out(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('index')

def pricing(request):
    services = Service.objects.all()
    return render(request, 'record/pricing.html', {'services': services})

def user(request):
    current_client = request.user

    client = Client.objects.get(email=current_client.email)
    records = Record.objects.filter(client=current_client.email)
    return render(request, 'record/user.html', {'client':client, 'records':records})

