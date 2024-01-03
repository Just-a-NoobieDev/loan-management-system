from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns =[
    path("", views.home, name="dashboard"),
    path("addClient", views.addClient, name="addClient"),
    path("addCollector", views.addCollector, name="addCollector"),
    path("delete/<int:id>", views.deleteClient, name="deleteClient"),
    path("generate/<int:id>", views.generateQR, name="generateQR"),
    # path("loanPortal", views.loanPortal, name="loanPortal"),
    # path("payments", views.payments, name="payments"),
    path("reports", views.reports, name="reports"),
    path("register", views.register, name="register"),
    path("adminLogin", views.adminLogin, name="adminLogin"),
    path('login-controller/', views.loginController, name='login-controller'),
    path('logout', views.logoutNow, name='logout'),
    path('client', views.client, name='client'),
    path('payment', views.payment, name='payment'),
    path('singleCollector', views.singleCollector, name='singleCollector'),
    path('generate/collector/<int:id>', views.generateCollector, name='generateCollector'),
    path("deleteCollector/<int:id>", views.deleteCollector, name="deleteCollector"),
    path('editClient', views.editClient, name='editClient'),
    path('editPayment', views.editPayment, name='editPayment'),
    path('loanList/', views.loan_list, name='loan_list'),
    path('addLoan/', views.add_loan, name='add_loan'),
    path('paymentList/', views.paymentList, name='paymentList'),
    path('addPayment/', views.addPayment, name='addPayment'),
    path('editCollector', views.editCollector, name='editCollector'),
    path('delete_payment/<int:id>/', views.delete_payment, name='delete_payment'),
    # path('edit_payment/<int:id>/', views.edit_payment, name='edit_payment'),
    #  path('delete_loan/<int:id>/', views.delete_loan, name='delete_loan'),
    path('exportTodayPayment', views.exportTodayPayments, name='exportTodayPayments'),
    path('exportTodayLoan', views.exportTodayLoans, name='exportTodayLoans'),
    path('exportLoan/<str:dateFrom>/<str:dateTo>/', views.exportLoans, name='exportLoans'),
    path('exportPayment/<str:dateFrom>/<str:dateTo>/', views.exportPayment, name='exportPayment'),
]