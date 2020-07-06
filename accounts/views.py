from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm


# Create your views here.
def indexView(request):
    return render(request, 'index.html')


@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')


def registerView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form=SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def createClass(request):
    return render(request,'classes/create.html')


def joinClass(request):
    return render(request,'classes/join.html')