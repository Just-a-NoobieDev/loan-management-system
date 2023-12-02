from django.shortcuts import render, HttpResponse

from .forms import PersonForm
from .models import Person


# Create your views here.
def home(request):
    return render(request, "dashboard.html")


def addClient(request):
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {'form': form}
            return render(request, "addClient.html", context)

    persons = Person.objects.all()
    context = {'form': PersonForm(), 'persons': persons}
    return render(request, "addClient.html", context)


def loanPortal(request):
    return render(request, "loanPortal.html")


def payments(request):
    return render(request, "payments.html")


def reports(request):
    return render(request, "reports.html")
