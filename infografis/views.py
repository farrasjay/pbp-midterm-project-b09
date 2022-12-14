import datetime, json
from urllib import response
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from infografis.models import *
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/uhealths/login/')
def infografis(request):
    return render(request, 'infografis.html')

@login_required(login_url='/uhealths/login/')
def first_artikel(request):
    return render(request, 'first-artikel.html')

@login_required(login_url='/uhealths/login/')
def second_artikel(request):
    return render(request, 'second-artikel.html')

@login_required(login_url='/uhealths/login/')
def third_artikel(request):
    return render(request, 'third-artikel.html')

@csrf_exempt
def add_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        date = datetime.date.today()
        user = request.user
        username = user.get_username()
        new_comment = Comment.objects.create(comment=comment, date=date, user=user, nama=username)

        result = {
            'fields':{
                'comment':new_comment.comment,
                'date':new_comment.date,
                'nama':request.user.get_username(),
            },
            'pk':new_comment.pk
        }

        print(result)
        return JsonResponse(result)

@csrf_exempt
def add_commentkedua(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        date = datetime.date.today()
        user = request.user
        username = user.get_username()
        new_comment = Commentkedua.objects.create(comment=comment, date=date, user=user, nama=username)

        result = {
            'fields':{
                'comment':new_comment.comment,
                'date':new_comment.date,
                'nama':request.user.get_username(),
            },
            'pk':new_comment.pk
        }

        print(result)
        return JsonResponse(result)

@csrf_exempt
def add_commentketiga(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        date = datetime.date.today()
        user = request.user
        username = user.get_username()
        new_comment = Commentketiga.objects.create(comment=comment, date=date, user=user, nama=username)

        result = {
            'fields':{
                'comment':new_comment.comment,
                'date':new_comment.date,
                'nama':request.user.get_username(),
            },
            'pk':new_comment.pk
        }

        print(result)
        return JsonResponse(result)

def show_json1(request):
    data = Comment.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json2(request):
    data = Commentkedua.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json3(request):
    data = Commentketiga.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def add_commentpertama_flutter(request):  #bener kan?
    body_unicode = (request.body.decode('utf-8'))
    body = json.loads(body_unicode)
    user = request.user
    date = datetime.date.today()
    username = user.get_username()
    comment = body['comment']
    new_comment = Comment.objects.create(comment=comment, date=date, user=user, nama=username)
        
    return HttpResponse(status=202)

@csrf_exempt
def add_commentkedua_flutter(request):  
    body_unicode = (request.body.decode('utf-8'))
    body = json.loads(body_unicode)
    user = request.user
    date = datetime.date.today()
    username = user.get_username()
    comment = body['comment']
    new_comment = Commentkedua.objects.create(comment=comment, date=date, user=user, nama=username)
        
    return HttpResponse(status=202)

@csrf_exempt
def add_commentketiga_flutter(request):  
    body_unicode = (request.body.decode('utf-8'))
    body = json.loads(body_unicode)
    user = request.user
    date = datetime.date.today()
    username = user.get_username()
    comment = body['comment']
    new_comment = Commentketiga.objects.create(comment=comment, date=date, user=user, nama=username)
        
    return HttpResponse(status=202)
