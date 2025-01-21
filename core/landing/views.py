from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render (request, "index.html")

def about(request):
    return render (request, "about.html")

def doctors(request):
    return render (request, "doctors.html")

def services(request):
    return render (request, "services.html")

def blog(request):
    return render (request, "blog.html")

    
def thanks(request):
    return render(request, "thanks.html", {})


