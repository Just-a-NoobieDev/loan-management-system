import os

from django.http import FileResponse
from django.shortcuts import render, HttpResponse, redirect

from django.conf import settings
from .forms import PersonForm
from .models import Person
from qrcode import *


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


def deleteClient(request, id):
    item = Person.objects.get(id=id)
    item.delete()
    os.remove(os.path.join(settings.MEDIA_ROOT, item.picture.name))
    os.remove(os.path.join(settings.MEDIA_ROOT, item.document.name))
    return redirect('/addClient')


def generateQR(request, id):
    person = Person.objects.get(id=id)
    img = make(person.id)
    img_url = 'qr-' + str(person.name) + '.png'
    img.save(settings.MEDIA_ROOT + '/qr/' + img_url)
    response = HttpResponse(img_url, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{img_url}"'
    return response


def loanPortal(request):
    return render(request, "loanPortal.html")


def payments(request):
    return render(request, "payments.html")


def reports(request):
    return render(request, "reports.html")
