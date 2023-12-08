from django.urls import path
from . import views

urlpatterns =[
    path("", views.home, name="home"),
    path("addClient", views.addClient, name="addClient"),
    path("delete/<int:id>", views.deleteClient, name="deleteClient"),
    path("generate/<int:id>", views.generateQR, name="generateQR"),
    path("loanPortal", views.loanPortal, name="loanPortal"),
    path("payments", views.payments, name="payments"),
    path("reports", views.reports, name="reports"),
    path("adminLogin", views.adminLogin, name="adminLogin"),
    path("clientLogin", views.clientLogin, name="clientLogin"),
]