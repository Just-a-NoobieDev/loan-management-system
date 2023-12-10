from django.shortcuts import redirect, render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Payment
from .forms import PaymentForm
from django.http import JsonResponse


# Create your views here.
def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'collectorDashboard.html', {'payments': payments})

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'redirect': '/collector/payment_list/'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def collectorLogin(request):
    return render(request, "collectorLogin.html")