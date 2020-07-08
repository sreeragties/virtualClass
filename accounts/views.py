from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,ClassesForm
from django.utils.crypto import get_random_string
from .models import Classes,Join
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def indexView(request):
    return render(request, 'index.html')


@login_required
def dashboardView(request):
    all_objects= Classes.objects.filter(user_id=request.user)
    classes= Join.objects.filter(user_id=request.user).values_list('class_code',flat=True)
    all_classes=Classes.objects.filter(code__in=classes)
    
    context= {'all_objects': all_objects,'all_classes':all_classes}
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

@login_required
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

@login_required
def joinClass(request):
    if request.method == "POST":
        try:
            code_name = request.POST['code']
            if Classes.objects.filter(code=code_name).exists():
                code = Classes.objects.get(code=code_name)
                if code.user_id==request.user:
                    messages.success(request, 'You Cannot Join The Class You Created')
                    return redirect('join_class')
                else:
                    p=Join(class_code=code,user_id=request.user)
                    p.save()
                    return redirect('dashboard')
            else:
                messages.success(request,'Class Do Not Exist')
                return redirect('join_class')
        except Exception:
            messages.success(request, 'You Joined This Class Already')
            return redirect('join_class')
    else:
        return render(request,'classes/join.html')

@login_required
def classView(request,class_code):
    classname = Classes.objects.get(code=class_code)
    ids = Join.objects.filter(class_code=class_code).values_list('user_id',flat=True)
    students = User.objects.filter(id__in=ids)
    return render(request, 'individual/class.html',{'students':students, 'classname':classname})

