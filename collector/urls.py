from django.urls import path
from . import views

urlpatterns = [
    path("", views.collectorLogin, name="login"),
    path("addPayment/", views.add_payment, name="add_payment"),
    path("payment_list/", views.payment_list, name="payment_list"),
    path("collector_login/", views.collector_login, name="collector_login"),
    path("logoutCollector/", views.logout_view, name="logoutCollector"),
]
