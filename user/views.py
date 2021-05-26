from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout,login

# Create your views here.
def signup(request):
    if request.method == 'POST':
            form=request.POST
            print(request.POST)   
            user_name = form['user_name']
            first_name = form['first_name']
            last_name = form['last_name']
            email = form['email']
            password=form['password']
            #pic=form['profile_pic']
            #pp=profile_pic()

            print(first_name, last_name, email)
            user=User()
            user.username=user_name
            user.first_name=first_name
            user.last_name=last_name
            user.set_password(password)
            user.email=email
            user.save()
            #pp.user=user
            #pp.pic=pic
            #pp.save()
            print(user)
            return HttpResponseRedirect('login')
    



    return render(request, "signup.html")


def login_user(request):
    user=request.user
    if user.id is not None:
        return HttpResponse('Already Logged in')
    if request.method=='POST':
        form=request.POST
        print(form)
        user_name=form['user_name']
        password=form['password']
        user=authenticate(request,username=user_name,password=password)
        print(user_name)
        print(password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/user'+'/'+str(user.id))
        else :
            return HttpResponse('invalid credentials')
            
  
    return render(request,"login.html")
@login_required
def user_details(request,id):
    user=User.objects.get(pk=id)
    #pic=profile_pic.objects.get(user=user)
    #profile=pic.pic.url
    print(user.last_name)
    return render(request,"profile.html",{'username':user.username,'fn':user.first_name,'ln':user.last_name,'email':user.email})

@login_required
def logout_user(request):
    user=request.user
    
    print(user)
    logout(request)
    return HttpResponse('successfully logged out see you next time ' +user.username)


def profile(request,id):
    user=User.objects.get(pk=id)
    