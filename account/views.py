from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import auth
from .forms import AccountAuthenticationForm
from .models import User
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages

def signin(request):
    context = {}
    if request.method=='POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            print('not valid')
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            print(user)
            if user:
                auth_login(request,user)
                if User.objects.filter(email=email,is_admin=True):
	                return HttpResponseRedirect(reverse('adminpage'))
                else:
                    return HttpResponseRedirect(reverse('home'))
        else:
            context['a'] = 'a'
    return render(request,"signin.html",context)
def signup(request):
    if request.method =='POST':
        Username = request.POST['fullname']
        birthday = request.POST['Date']
        phonenumber = request.POST['Phonenumber']
        email = request.POST['email']
        password = request.POST['pass']
        if User.objects.filter(email=email).exists():
            messages.info(request,'email taken')
            return redirect('/account/signup')
        elif len(password)<6:
            messages.info(request,'plear enter perfect pass')
            return redirect('/account/signup')
        else:
            user=User.objects.create_user(email=email,username=Username,birthday=birthday,phonenumber=phonenumber,password=password)
            user.save()
            auth.login(request,user)
            return HttpResponseRedirect(reverse('signin'))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('signin'))