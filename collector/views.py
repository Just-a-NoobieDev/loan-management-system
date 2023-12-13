from django.shortcuts import redirect, render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from loanmanagement.models import Payment, Loan
from loanmanagement.forms import PaymentForm, LoanForm
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth, messages


# Create your views here.
def payment_list(request):
    loans = Loan.objects.all()
    paginated = Paginator(loans, 2)
    page_number = request.GET.get('page')
    page = paginated.get_page(page_number)
    form = PaymentForm(request.POST)
    
    return render(request, 'collectorDashboard.html', {'loans': page, 'form': form, 'paginator': paginated})


def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            loan = payment.loan_id
            loan.loan_balance -= payment.amount
            loan.save()
            payment.save()
            messages.success(request, 'Payment added successfully.')
            return JsonResponse({'status': 'success', 'redirect': 'payment_list/'})
    else:
        form = PaymentForm()

    return render(request, 'collectorDashboard.html', {'form': form})

def collectorLogin(request):
    return render(request, "collectorLogin.html")