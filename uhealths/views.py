import datetime, json, logging
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def landingpage(request):
    return render(request, 'home.html')

def register(request):
    # logger = logging.getLogger(__name__)
    # logger.debug("MASUK REGISTER")
    # print("MASUK REGISTER")

    form = UserCreationForm()

    if request.method == "POST":
        # print(form.is_valid())
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil teregister!')
            return redirect('uhealths:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("uhealths:menu"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('uhealths:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/uhealths/login/')
def main_menu(request):
    return render(request, "menu.html")