from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
    student = Student.objects.all()
    return render(request, 'index.html', {'students' : student})