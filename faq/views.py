from django.shortcuts import render
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
import requests

from faq.models import Question, Like

# @login_required(login_url='/uhealths/login/')
def show_faq_page(request):
    data_faq = Question.objects.all()
    status_user = False
    user = request.user
    if request.user.is_authenticated:
        status_user = True
    context = {
    'data_faq': data_faq,
    'status_user' : status_user,
    'user': user
    }
    return render(request, "faq.html", context)

def set_session(request, id):
    data_faq = Question.objects.all()
    status_user = False
    user = request.user
    if request.user.is_authenticated:
        status_user = True
    recently_viewed_question = None

    if 'recently_viewed_ques' in request.session:
        if id in request.session['recently_viewed_ques']:
            request.session['recently_viewed_ques'].remove(id)
        else:
            request.session['recently_viewed_ques'].insert(0, id)
        recently_viewed_question = list(request.session['recently_viewed_ques'])
    else:
        request.session['recently_viewed_ques'] = [id]
        recently_viewed_question = list(request.session['recently_viewed_ques'])


    request.session.modified = True
    context = {
        'recently_viewed_question': recently_viewed_question
    }
    # return render(request, 'faq.html', context)
    return JsonResponse(context)

def get_session(request):
    if 'recently_viewed_ques' in request.session:
        recently_viewed_question = list(request.session['recently_viewed_ques'])
    else:
        recently_viewed_question = None
    context = {
        'recently_viewed_question': recently_viewed_question
    }
    return JsonResponse(context)



def like_unlike_post(request, id):
    user = request.user
    if request.method == 'POST':
        if request.user.is_authenticated:
            question_obj = Question.objects.get(id=id)
            
            if user in question_obj.liked.all():
                question_obj.liked.remove(user)
                question_obj.num_liked = question_obj.num_liked -1
            else:
                question_obj.liked.add(user)
                question_obj.num_liked = question_obj.num_liked +1

            question_obj.save()
            return redirect('faq:faq')

    return redirect('faq:faq')