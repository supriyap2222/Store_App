from django.shortcuts import render,redirect
from .forms import RegisterForm
from django import forms
from .models import Account
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage , send_mail



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
            # print(password)
            user = Account.objects.create_user(first_name=first_name, 
                                               last_name=last_name , 
                                               email=email, 
                                               username=username, 
                                               password=password,
                                               )
            # we r giving user.phone_number because in models.py there is no phonenumber in def createuser
            user.phone_number=phone_number
            user.save()

            # User activation - after saving the 'user'  object
            current_site = get_current_site(request)
            subject = 'Please activate your account'
            # message = render_to_string('hloo,please verify')
            message = render_to_string('accounts/account_verification_email.html',{
                            # 'user': user.first_name,
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            # (up)we are encoding user-primarykey so nobody can see primary key
                'token': default_token_generator.make_token(user),
                            # (make_token is function which will create token of particular user) 
            })
                            # now send email
            print(message)
            to_email = email
            from_email = 'aakash.singh.as140@gmail.com'
            # recipient_list = [to_email,'aksh.singh2222@gmail.com']
            recipient_list = [to_email]
            print(recipient_list)
            # recipient_list = ['aakash.singh.as130@gmail.com']
            send_email = EmailMessage(subject, message, to=[to_email])
            send_email.send()
            # send_mail(subject, message, from_email, recipient_list)

            # messages.success(request, 'Thank you !! Verification sent to Email, please verify!')
            # return redirect('register') 
            return redirect('/accounts/login/?command=verification&email='+email)
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
        email = request.POST.get('email')
        password = request.POST['password']
        # hashpassword = set_password(password)
        
        # user = auth.authenticate(email='email', password='password')
        # user = auth.authenticate(email=email, password=password)
        # users = Account.objects.values('email','password')
        # print(users)
        user = Account.objects.filter(email=email, password=password)
        print(user)        
        # print({{user.first_name}})
        # user = authenticate(request, email=email, password=password)
        print(user)
        # this will return the user-object
        if user:
        # if user is not None:
            # auth.login(request, user)
            messages.success(request, 'You are logged In.')
            # print(user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
    return render(request, 'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')


def activate(request, uidb64 ,token):
    # return HttpResponse('ok')
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
                    # here we r taking primary key of user
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations !!!, Your account is activated.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid Activation Link')
        return redirect('register')
        

@login_required(login_url= 'login')
def dashboard(request):

    return render(request, 'accounts/dashboard.html')