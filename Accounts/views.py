from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
        if request.method == 'POST':
                #The user has information and wants to create an account
                if request.POST['password1'] == request.POST['password2'] :
                        try:
                                user = User.objects.get(username=request.POST['username'])
                                return render(request , 'Accounts/signup.html' , {'error' : 'username has already been taken'})

                        except User.DoesNotExist :
                                user = User.objects.create_user(request.POST['username'] , password=request.POST['password1'])
                                auth.login(request , user)
                                return redirect('home')
                else :
                        return render(request , 'Accounts/signup.html' , {'error' : 'Passwords must match'})

        else:
                return render(request , 'Accounts/signup.html')

def login(request):
        if request.method == 'POST':
                pass
        else:
                return render(request , 'Accounts/login.html')

def logout(request):
    # TODO need to route to homepage
    return render(request , 'Accounts/signup.html')