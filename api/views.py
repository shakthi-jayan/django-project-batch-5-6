from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

# Create your views here.
def student_list(request):
    students = Student.objects.all()
    return render(request, "students/list.html",{"students" : students})

def create_student(request):
    if request.method == "POST":
        form = StudentForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(
        request,
        'students/create.html',
        {'form': form}
    )
