from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    form=StudentForm(request.POST)
    stud=Student.objects.all()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New Student registered Successfully !!!")
            return redirect('viewlist')
    context={'form':form}
    return render(request,"register.html",context=context)


def viewlist(request):
    stud=Student.objects.all()  
    context={'stud':stud}
    return render(request, 'viewlist.html',context=context)

def updatelist(request,pk):
    stud=Student.objects.get(id=pk)
    form= StudentForm(request.POST or None,instance=stud)
    if request.method=='POST':
        form= StudentForm(request.POST,instance=stud)
        if form.is_valid():
            form.save()
            messages.success(request, "Student data updated Successfully !!!")
            return redirect('viewlist')
    context={'form':form}
    return render(request, 'updatelist.html',context=context)



def deletelist(request,pk):
    stud=Student.objects.get(id=pk)   
    if request.method=='POST':
        stud.delete()
        messages.success(request, "Student Data Deleted Successfully !!!")
        return redirect('viewlist')
    
    context={'object':stud}
    return render(request, 'deletelist.html',context=context)
