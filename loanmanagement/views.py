from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request, "dashboard.html")
def addClient(request):
    return render(request, "addClient.html")
def loanPortal(request):
    return render(request, "loanPortal.html")

def payments(request):
    return render(request, "payments.html")

def reports(request):
    return render(request, "reports.html")