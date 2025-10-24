from django.shortcuts import render
from .models import*
from .forms import *

# Create your views here.

def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)  # include request.FILES
        if form.is_valid():
            form.save()
            return redirect('login')  # make sure you have a login URL
    else:
        form = RegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})