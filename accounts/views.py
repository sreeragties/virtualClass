from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,ClassesForm
from django.utils.crypto import get_random_string
from .models import Classes,Join
from django.contrib import messages


# Create your views here.
def indexView(request):
    return render(request, 'index.html')


@login_required
def dashboardView(request):
    all_objects= Classes.objects.all()
    
    context= {'all_objects': all_objects}
    return render(request, 'dashboard.html', context)


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
    if request.method == "POST":
        form = ClassesForm(request.POST)
        if form.is_valid():
            classes = form.cleaned_data['classes']
            teacher = form.cleaned_data['teacher']
            subject = form.cleaned_data['subject']
            code = get_random_string(length=5)
            p = Classes(classes=classes, teacher=teacher, subject=subject, code=code , user_id=request.user)
            p.save()
            return redirect('dashboard')
    else:
        form = ClassesForm()
    return render(request,'classes/create.html',{'form': form})


def joinClass(request):
    if request.method == "POST":
        code_name = request.POST['code']
        if Classes.objects.filter(code=code_name).exists():
            code = Classes.objects.get(code=code_name)
            p=Join(class_code=code,user_id=request.user)
            p.save()
            return redirect('dashboard')
        else:
            messages.success(request,'Class Do Not Exist')
            return redirect('join_class')
    else:
        return render(request,'classes/join.html')

