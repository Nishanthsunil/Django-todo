from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect

def logout(request):
    auth.logout(request)
    return redirect('login')
    