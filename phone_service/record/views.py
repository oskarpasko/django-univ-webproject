from django.shortcuts import render, redirect
from .models import *
from .forms import LoginForm, RegisterForm, RecordForm, UpdateForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'record/register.html', { 'form': form}) 
    
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'record/register.html', {'form': form})

def index(request):
    locations = Location.objects.all()

    return render(request, "record/index.html", {"locations":locations})

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
    services = Service.objects.all().order_by('name')
    return render(request, 'record/pricing.html', {'services': services})

@login_required
def user(request):
    current_client = request.user

    client = Client.objects.get(email=current_client.email)
    records = Record.objects.filter(client=current_client.email).order_by('-start_date')
    discount = Record.objects.filter(client=current_client.email).aggregate(Sum('price'))
    if discount['price__sum'] < 1000:
        to_discount = round(Decimal(1000) - discount['price__sum'], 2)
    elif discount['price__sum'] >= Decimal(1000) and discount['price__sum'] < Decimal(2000):
        to_discount = round(Decimal(2000) - discount['price__sum'], 2)
    elif discount['price__sum'] >= Decimal(2000) and discount['price__sum'] < Decimal(3000):
        to_discount = round(Decimal(3000) - discount['price__sum'], )
    elif discount['price__sum'] >= Decimal(3000) and discount['price__sum'] < Decimal(4000):
        to_discount = round(Decimal(4000) - discount['price__sum'], 2)
    else:
        to_discount = False
    return render(request, 'record/user.html', {'client':client, 'records':records, 'discount':discount, 'to_discount':to_discount})

@login_required
def new_record(request):
    if request.method == 'GET':
            form = RecordForm()
            return render(request, 'record/new_record.html', { 'form': form}) 
    
    if request.method == 'POST':
        form = RecordForm(request.POST)
        current_client = request.user
        client = Client.objects.get(email=current_client.email)
        service = Service.objects.get(id = request.POST.get('service'))
        location = Location.objects.get(id = request.POST.get('locations'))
        country = Location.objects.values('country').get(id = request.POST.get('locations'))

        discount = Record.objects.filter(client=current_client.email).aggregate(Sum('price'))

        if country['country'] == 'Poland':
            price = Service.objects.values('price').get(id = request.POST.get('service'))

            if discount['price__sum'] >= Decimal(1000) and discount['price__sum'] < Decimal(2000):
                price = (Decimal(price['price']) * Decimal(3.09)) * Decimal(0.9)
            elif discount['price__sum'] >= Decimal(2000) and discount['price__sum'] < Decimal(3000):
                price = (Decimal(price['price']) * Decimal(3.09)) * Decimal(0.8)
            elif discount['price__sum'] >= Decimal(3000) and discount['price__sum'] < Decimal(4000):
                price = (Decimal(price['price']) * Decimal(3.09)) * Decimal(0.7)
            elif discount['price__sum'] > Decimal(4000):
                price = (Decimal(price['price']) * Decimal(3.09)) * Decimal(0.6)
            else:
                price = Decimal(price['price'])

        else:
            price = Service.objects.values('price').get(id = request.POST.get('service'))

            if discount['price__sum'] >= Decimal(1000) and discount['price__sum'] < Decimal(2000):
                price = Decimal(price['price']) * Decimal(0.9)
            elif discount['price__sum'] >= Decimal(2000) and discount['price__sum'] < Decimal(3000):
                price = Decimal(price['price']) * Decimal(0.8)
            elif discount['price__sum'] >= Decimal(3000) and discount['price__sum'] < Decimal(4000):
                price = Decimal(price['price']) * Decimal(0.7)
            elif discount['price__sum'] > Decimal(4000):
                price = Decimal(price['price']) * Decimal(0.6)
            else:
                price = Decimal(price['price'])


        record = Record.objects.create(start_date = request.POST.get('start_date'), deadline = None, price = price, client = client, service = service, location = location)
        record.save()
        return redirect('index')

@login_required
def update(request):
    form = UpdateForm()
    current_client = request.user

    client = Client.objects.get(email=current_client.email)
    return render(request, 'record/update.html', {'client':client, 'form':form})
