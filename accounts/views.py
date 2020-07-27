from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,ClassesForm,NotesForm,AssignmentForm
from django.utils.crypto import get_random_string
from .models import Classes,Join,Notes,Assignment,SubmitAssignment
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

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
        else:
            messages.error(request, 'Invalid Login Credentials')
            return redirect('login_url')

    return render(request,'registration/login.html')

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
    notes = Notes.objects.filter(class_code=class_code)
    assignments = Assignment.objects.filter(class_code=class_code)
    return render(request, 'individual/class.html',{'students':students, 'classname':classname, 'notes':notes, 'assignments':assignments})

@login_required
def joinView(request,class_code):
    classname = Classes.objects.get(code=class_code)
    ids = Join.objects.filter(class_code=class_code).values_list('user_id',flat=True)
    students = User.objects.filter(id__in=ids)
    notes = Notes.objects.filter(class_code=class_code)
    assignments = Assignment.objects.filter(class_code=class_code)
    submit_assignments = SubmitAssignment.objects.filter(assignment__in=assignments)
    return render(request, 'individual/join.html',{'students':students, 'classname':classname, 'notes':notes,'assignments':assignments,'submitted_assignments':submit_assignments})

@login_required
def noteUpload(request,class_code):
    classname = Classes.objects.get(code=class_code)
    if request.method == "POST":
        form = NotesForm(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            file = request.FILES.get('file')
            p = Notes(class_code=classname, title = title, desc = desc, file = file)
            p.save()
            return redirect('class_page',class_code=class_code)
    else:
        form = NotesForm()
    return render(request,'notes/notes.html',{'form':form, 'classname':classname})

@login_required
def noteDelete(request,class_code,note_id):
    Notes.objects.get(pk=note_id).delete()
    return redirect('class_page',class_code=class_code)

@login_required
def assignmentUpload(request,class_code):
    classname = Classes.objects.get(code=class_code)
    if request.method == "POST":
        form = AssignmentForm(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            file = request.FILES.get('file')
            last_date=form.cleaned_data['last_date']
            max_marks=form.cleaned_data['max_marks']
            p = Assignment(class_code=classname, title = title, desc = desc, file = file,last_date=last_date,max_marks=max_marks)
            p.save()
            return redirect('class_page',class_code=class_code)
    else:
        form = AssignmentForm()
    return render(request,'notes/assignment.html',{'form':form, 'classname':classname})

@login_required
def submitAssignment(request,assignment_id):
    class_code = Assignment.objects.filter(pk=assignment_id).values_list('class_code',flat=True)[0]
    if request.method == "POST":
        file = request.FILES.get('file')
        p = SubmitAssignment(assignment_id=assignment_id,user_id=request.user,submitted_file=file)
        p.save()
        return redirect('join_page',class_code=class_code)
    return render(request,'notes/submit.html',{'assignment_id':assignment_id})

@login_required
def unsubmitAssignment(request,assignment_id,submitted_id):
    class_code = Assignment.objects.filter(pk=assignment_id).values_list('class_code',flat=True)[0]
    SubmitAssignment.objects.get(pk=submitted_id).delete()
    return redirect('join_page',class_code=class_code)

@login_required
def assignmentDelete(request,class_code,assignment_id):
    Assignment.objects.get(pk=assignment_id).delete()
    return redirect('class_page',class_code=class_code)

@login_required
def classDelete(request,class_code):
    Classes.objects.get(pk=class_code).delete()
    return redirect('dashboard')

@login_required
def classUnenroll(request,class_code):
    Join.objects.get(class_code_id=class_code,user_id=request.user).delete()
    return redirect('dashboard')

