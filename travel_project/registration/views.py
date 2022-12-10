from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=user_name, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "Invalid user")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password1']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name,
                                            email=email)
                user.save()

                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
