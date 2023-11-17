# myapp/views.py

from django.shortcuts import render, redirect
from todo.forms import NewUserForm
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Success')
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid Information")
    else:  # Fix: Added the else part to instantiate the form for GET requests
        form = NewUserForm()
    return render(request, "registration/signup.html", {"register_form": form})
