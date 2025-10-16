from pyexpat.errors import messages
from sqlite3 import IntegrityError
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Student
from django.contrib import messages

# Create your views here.
def home(request):
    student = Student.objects.all()
    return render(request, 'index.html', {'students' : student})


def delete_student(request , id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('home')

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')

        if Student.objects.filter(email=email).exists():
            messages.error(request, "Email already exists! Please use a different email.")
            return redirect('home')

        Student.objects.create(name=name, email=email, age=age)
        messages.success(request, "Student added successfully!")
        return redirect('home')

def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.age = request.POST['age']
        student.save()
        return redirect('home')
    return render(request, 'home.html', {'student': student})
