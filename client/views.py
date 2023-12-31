from django.shortcuts import render, redirect
from django.http import JsonResponse
from loanmanagement.models import Loan, Payment, Person
from django.contrib import messages

from client.forms import LoginForm


# Create your views here.
def login(request):
    login_form = LoginForm(request.POST)
    return render(request, "login.html", {'form': login_form})


def dashboard(request):
    return render(request, "clientDashboard.html")


def get_loan_balance(request, id):
    loan = {}
    try:
        loan = Loan.objects.get(client_id=id)
        loan_balance = loan.loan_balance
        payments = Payment.objects.filter(loan_id=loan.id)
    except Loan.DoesNotExist:
        loan_balance = "Client not found or no loan information available"
        payments = []

    return render(
        request,
        "clientDashboard.html",
        {"loan": loan, "loan_balance": loan_balance, "payments": payments},
    )


def client_login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("pass")
        try:
            person = Person.objects.get(email=name)
            if person.password == password:
                request.session["user_id"] = person.id
                messages.success(request, "Login successful!")
                return redirect(f"/loan/{person.id}/")
        except Person.DoesNotExist:
            error_message = "Name not found. Please try again."
            return render(request, "login.html", {"error_message": error_message})
    return render(request, "login.html")


def logout_view(request):
    # Log out the user (for the sake of example)
    # In a real-world scenario, you would use Django's authentication system
    # For simplicity, we're just deleting the session variable here
    del request.session["user_id"]
    return redirect("/")
