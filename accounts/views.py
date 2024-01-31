from django.shortcuts import render,redirect
from .forms import RegisterForm
from django import forms
from .models import Account
from django.contrib import messages,auth
from django.contrib import auth

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # registrationForm is inside form.py file
        if form.is_valid():
            # just creating user
            first_name      = form.cleaned_data['first_name']
            last_name       = form.cleaned_data['last_name']
            email           = form.cleaned_data['email']
            phone_number    = form.cleaned_data['phone_number']
            password        = form.cleaned_data['password']
            confirm_password= form.cleaned_data['confirm_password']
            # below line will take username as 'aakash' from 'aakash@gmail.com'
            username        = email.split('@')[0]
            print(password)
            user = Account.objects.create_user(first_name=first_name, 
                                               last_name=last_name , 
                                               email=email, 
                                               username=username, 
                                               password=password,
                                               )
            # we r giving user.phone_number because in models.py there is no phonenumber in def createuser
            user.phone_number=phone_number
            user.save()
            messages.success(request, 'Registration Successfull.')
            return redirect('register')
        # to return on same page
    else:
        # registration form should render if 'get' request
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html',context)





def login(request):
    if request.method == 'POST':
        # email is name inside input feild in login.html-form
        email = request.POST['email']
        password = request.POST['password']
        # hashpassword = set_password(password)
        # print(hashpassword)
        print(email)
        print(password)
        # user = auth.authenticate(email='email', password='password')
        # user = auth.authenticate(email=email, password=password)
        users = Account.objects.values('email','password')
        print(users)
        user = Account.objects.filter(email=email, password=password)
        print(user)
        # this will return the user-object
        if user:
        # if user is not None:
            # auth.login(request, user)
            messages.success(request, 'You are logged In.')
            # print(user)
            return redirect('login')
        else:
            messages.error(request, 'Invalid login credentials')
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')