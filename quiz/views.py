from django.db.models.manager import EmptyManager
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from user.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login


# Create your views here.
@login_required
def showquiz(request,quiz_id):
    quiz=Quiz.objects.get(pk=quiz_id)
    questions=quiz.questions.all()
    user=request.user
    session_id = 'Quiz'+':'+str(quiz_id)+':'+str(user.id)
    if request.session.get(session_id)==quiz.enrollment_key:
     return render(request,'quiz.html',{'questions':questions})
    return redirect('check', quiz_id)
@login_required
def enrollment_key_checker(request,quiz_id):
 if request.method=='POST':
     form = request.POST
     enrollment_key=form['enrollment_key']
     quiz=Quiz.objects.get(pk=quiz_id)
     user=request.user
     if enrollment_key==quiz.enrollment_key:
      session_id='Quiz'+':'+str(quiz_id)+':'+str(user.id)
      request.session[session_id]=enrollment_key
      return redirect('test', quiz_id)
     else:
      return HttpResponse('invalid')
    





 return render(request,'quizverify.html')
     

