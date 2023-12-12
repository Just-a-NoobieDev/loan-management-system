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
    path("loanPortal", views.loanPortal, name="loanPortal"),
    path("payments", views.payments, name="payments"),
    path("reports", views.reports, name="reports"),
    path("register", views.register, name="register"),
    path("adminLogin", views.adminLogin, name="adminLogin"),
    path('login-controller/', views.loginController, name='login-controller'),
    path('logout', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('client', views.client, name='client'),
    path('singleCollector', views.singleCollector, name='singleCollector'),
    path('generate/collector/<int:id>', views.generateCollector, name='generateCollector'),
    path("deleteCollector/<int:id>", views.deleteCollector, name="deleteCollector"),
    path('editClient', views.editClient, name='editClient'),
    path('editCollector', views.editCollector, name='editCollector')
]