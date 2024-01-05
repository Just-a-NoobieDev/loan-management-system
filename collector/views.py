from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from collector.forms import LoginForm
from loanmanagement.models import Payment, Loan, Collector
from loanmanagement.forms import PaymentForm, LoanForm
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth, messages
from django.http import HttpResponse


# Create your views here.
def payment_list(request):
    loans = Loan.objects.all()
    paginated = Paginator(loans, 10)
    page_number = request.GET.get("page")
    page = paginated.get_page(page_number)
    form = PaymentForm(request.POST)

    return render(
        request,
        "collectorDashboard.html",
        {"loans": page, "form": form, "paginator": paginated},
    )


def add_payment(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            loan = payment.loan_id
            loan.loan_balance -= payment.amount
            loan.save()
            payment.save()
            messages.success(request, "Payment added successfully.")
            return JsonResponse({"status": "success", "redirect": "payment_list/"})
    else:
        form = PaymentForm()

    return render(request, "collectorDashboard.html", {"form": form})


def collectorLogin(request):
    login_form = LoginForm(request.POST)
    return render(request, "collectorLogin.html", {"form": login_form})


def collector_login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("pass")
        try:
            person = Collector.objects.get(email=name)
            if person.password == password:
                messages.success(request, "Login successful!")
                return redirect("payment_list/")
        except Collector.DoesNotExist:
            error_message = "Name not found. Please try again."
            return render(request, "/collector/", {"error_message": error_message})
    return render(request, "collectorLogin.html")


def logout_view(request):
    return redirect("/collector/")
