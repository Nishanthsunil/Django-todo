from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect



def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('todo:lists')
        else:
            messages.info(request,"Invalid credential")
            return redirect("login")
    return render(request,'registration/login.html')