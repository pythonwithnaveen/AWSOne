from django.shortcuts import render
from app20.forms import StudentForm
from app20.forms import CourseForm
from app20.models import StudentModel
from app20.models import CourseModel

# Create your views here.
def showIndex(request):
    return render(request,"index.html",{"c_form":CourseForm()})


def showStudent(request):
    return render(request, "studnet.html", {"s_form": StudentForm()})