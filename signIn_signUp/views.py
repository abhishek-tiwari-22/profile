from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages


def signin(request):

    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        request.session.modified=True
        request.session['email']=email

        user=Details(email=email,password=password)

        if Details.objects.filter(email=email,password=password).exists():
            Details.objects.get(email=email,password=password)
            return redirect('/profile')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/')

    return render(request, 'signIn_signUp/signin.html')


def signup(request):

    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        address=request.POST['address']

        if password1==password2:
            if Details.objects.filter(username=username).exists():
                messages.info(request, "UserName Taken")
                return redirect('/signup')
            elif Details.objects.filter(email=email).exists():
                messages.info(request, "Email Already in use")
                return redirect('/signup')
            user=Details.objects.create(
                username=username,password=password1,email=email,address=address
            )
            user.save()
            return redirect('/')
        else:
            messages.info(request, "Both Passwords did not match")
            return redirect('/signup')
    else:
        return render(request, 'signIn_signUp/signup.html')

def profile(request):
    mail=request.session['email']
    user=Details.objects.get(email=mail)
    return render(request,'signIn_signUp/profile.html',{'user':user})

def edit(request):
    mail=request.session['email']
    user1=Details.objects.get(email=mail)
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        address=request.POST['address']
        if user1.username==username and user1.password==password and user1.email==email and user1.address==address:
            messages.info(request, "Make Changes")
            return redirect('/profile/edit')
        elif Details.objects.filter(username=username) and user1.username!=username:
            messages.info(request, "UserName Taken")
            return redirect('/profile/edit')
        elif Details.objects.filter(email=email) and user1.email!=email:
            messages.info(request, "Email Taken")
            return redirect('/profile/edit')

        user1.username=username
        user1.email=email
        user1.password=password
        user1.address=address
        user1.save()
        request.session.modified=True
        request.session['email']=email
        return redirect('/')
        
    return render(request, 'signIn_signUp/edit.html')

def delete(request):
    mail=request.session['email']
    user=Details.objects.get(email=mail)
    user.delete()
    return render(request, 'signIn_signUp/deleted.html')
