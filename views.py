from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Intake

def display(request):
    return render(request, "display.html")

def getting(request):
    id = request.POST.get("id")
    name = request.POST.get("name")
    age = request.POST.get("age")
    email = request.POST.get("email")
    mobile = request.POST.get("mobile")
    date_of_birth = request.POST.get("date_of_birth")
    gender = request.POST.get("gender")
    division = request.POST.get("division")
    firstvote = request.POST.get("ft")
    newentry = Intake(id=id, name=name, age=age, email=email, mobile=mobile, date_of_birth=date_of_birth, gender=gender, division=division, firstvote=firstvote)
    newentry.save()
    answer = "done"
    return render(request, "display.html", {'res': answer})

def showlist(request):
    obj = Intake.objects.all()
    return render(request, "display2.html", {'toshow': obj})

def update_entry(request, id):
    entry = get_object_or_404(Intake, id=id)
    if request.method == "POST":
        entry.name = request.POST.get("name")
        entry.mobile = request.POST.get("mobile")
        entry.division = request.POST.get("division")
        entry.firstvote = request.POST.get("ft")
        entry.save()
        return redirect('showlist')
    return render(request, "update.html", {'entry': entry})

def delete_entry(request, id):
    entry = get_object_or_404(Intake, id=id)
    entry.delete()  # Soft delete logic can be implemented if necessary
    return redirect('showlist')
