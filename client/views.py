from django.shortcuts import render

from client.forms import LoginForm


# Create your views here.
def login(request):
    login_form = LoginForm(request.POST)
    return render(request, "login.html", {'form': login_form})
