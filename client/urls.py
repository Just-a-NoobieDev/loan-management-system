from django.urls import path
from . import views

urlpatterns = [
    path("", views.client_login, name="client_login"),
    path("logoutClient/", views.logout_view, name="logoutClient"),
    # path("dashboard/", views.dashboard, name="dashboard"),
    path("loan/<int:client_id>/", views.get_loan_balance, name="get_loan_balance"),
]
