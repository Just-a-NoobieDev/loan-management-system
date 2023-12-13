import base64
import io
import json
import os
from io import BytesIO
import mimetypes
from wsgiref.util import FileWrapper

from django.conf.global_settings import MEDIA_ROOT, MEDIA_URL
from django.contrib import auth, messages
from django.contrib.auth import logout, authenticate, login
from django.http import FileResponse
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.conf import settings

from elective5.settings import BASE_DIR
from .forms import PersonForm, UserRegistration, LoanForm, PaymentForm
from .models import Person, Loan, Payment
from qrcode import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('adminLogin')
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
    if item.picture.name and item.document.name:
        os.remove(os.path.join(settings.MEDIA_ROOT, item.picture.name))
        os.remove(os.path.join(settings.MEDIA_ROOT, item.document.name))
    return redirect('/adminUser/addClient')


def qrFunc(val, name):
    img = make(val)
    img_url = 'qr-' + str(name) + '.png'
    # buffer = io.BytesIO()
    img.save(settings.MEDIA_ROOT + '/qr/' + img_url)
    return img_url


def generateQR(request, id):
    person = Person.objects.get(id=id)
    img = qrFunc(person.id, person.name)
    # # qrcode = base64.b64encode(buffer.getvalue()).decode("utf-8")
    if img:
        wrapper = FileWrapper(open(settings.MEDIA_ROOT + "/qr/" + img, 'rb'))
        content_type = mimetypes.guess_type(img)[0]
        response = HttpResponse(wrapper, content_type=content_type)
        response['Content-Disposition'] = "attachment; filename=%s" % img
        return response

def loan_list(request):
    loans = Loan.objects.all()
    paginated = Paginator(loans, 15)
    page_number = request.GET.get('page')
    page = paginated.get_page(page_number)
    form = LoanForm(request.POST)
    
    return render(request, 'loanPortal.html', {'loans': page, 'form': form, 'paginator': paginated})

def add_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.loan_balance += loan.loan_balance
            loan.save()
            messages.success(request, 'Loan added successfully.')
            return JsonResponse({'status': 'success', 'redirect': 'loanList/'})
    else:
        form = LoanForm()

    return render(request, 'loanPortal.html', {'form': form})


def collectorLogin(request):
    return render(request, "collectorLogin.html")

# def loanPortal(request):
#     return render(request, "loanPortal.html")


def paymentList(request):
    payments = Payment.objects.all()
    paginated = Paginator(payments, 5)
    page_number = request.GET.get('page')
    page = paginated.get_page(page_number)
    form = PaymentForm(request.POST)
    
    return render(request, 'payments.html', {'payments': page, 'form': form, 'paginator': paginated})


def addPayment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            loan = payment.loan_id
            loan.loan_balance -= payment.amount
            loan.save()
            payment.save()
            messages.success(request, 'Payment added successfully.')
            return JsonResponse({'status': 'success', 'redirect': 'paymentList/'})
    else:
        form = PaymentForm()

    return render(request, 'payments.html', {'form': form})

# def payments(request):
#     posts = Payment.objects.all()
#     paginated = Paginator(posts, 3)
#     page_number = request.GET.get('page') #Get the requested page number from the URL
    
#     page = paginated.get_page(page_number)
#     return render(request, 'adminUser/paymentList', {'page':page})

def reports(request):
    return render(request, "reports.html")


def register(request):
    user = request.user
    if user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        # else:
        #     raise Exception(form.errors.get_text())
    else:
        form = UserRegistration()
    return render(request, 'register.html', {'form': form})


def adminLogin(request):
    user = request.user
    if user.is_authenticated:
        return redirect('dashboard')
    return render(request, "adminLogin.html")


def loginController(request):
    logout(request)
    resp = {"status": 'failed', 'msg': ''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['user']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status'] = 'success'
            else:
                resp['msg'] = 'Incorrect username or password'
        else:
            resp['msg'] = 'Incorrect username or password'
    return HttpResponse(json.dumps(resp), content_type="application/json")


def logout_page(request):
    auth.logout(request)
    return redirect('/adminUser/adminLogin/')


def client(request):
    id = request.POST.get('id')
    client_data = Person.objects.get(id=id)
    client_json = {
        'name': client_data.name,
        'address': client_data.address,
        'image': '/media/' + client_data.picture.name,
        'document': '/media/' + client_data.document.name
    }
    return HttpResponse(json.dumps(client_json), content_type="application/json")
