from django.http import HttpResponse
from canteen.models import *
from .forms import CommentForm
from .models import Drink
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'canteen/index.html')



def account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('account')
    else:
        form = UserCreationForm()

    return render(request, 'canteen/account.html', {'form': form})




def signin(request):
    return render(request, 'canteen/signin.html')


def pages(request, pid): #HTTPRequest
    return HttpResponse(f"<h1>Страница </h1> <p>{pid}</p>")


def about(request): # render
    return render(request, 'canteen/about.html')


def orders_page(request):
    return render(request, 'canteen/orders.html', {'orders': SalesOrder.objects.all()})


def menu(request):
    return render(request, 'canteen/menu.html')


def info_order(request):
    return render(request, 'canteen/info_order.html', {'order': SalesOrder.objects.all()[0].food.all()[0]})




def eat(request):
    if 'search' in request.GET:
        search = request.GET['search']
        multiple_search = Q(Q(name__icontains=search) | Q(description__icontains=search))
        eatt = Eat.objects.filter(multiple_search)
    elif 'max' in request.GET:
        max = request.GET['max']
        eatt = Eat.objects.filter(price__lte=max)
    else:
        eatt = Eat.objects.all()
    return render(request, 'canteen/eat.html', {"eatt": eatt})




def drink(request):
    if 'search' in request.GET:
        search = request.GET['search']
       #pics = Drink.objects.filter(name__icontains=search)
        multiple_search = Q(Q(name__icontains=search) | Q(description__icontains=search))
        drin = Drink.objects.filter(multiple_search)
    elif 'max' in request.GET:
        max = request.GET['max']
        drin = Drink.objects.filter(price__lte=max)
    else:
        drin = Drink.objects.all()
    return render(request, 'canteen/drink.html', {"pics": drin})


def abou(request):
    new =Comment.objects.order_by('-id')
    return render(request, 'canteen/about.html', {'news': new})

def about(request):
        error = ''
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/news')
            else:
                error = 'Форма была неверной'

        form = CommentForm()
        data = {
            'form': form,
            'error': error
        }
        return render(request, 'canteen/about.html',data)