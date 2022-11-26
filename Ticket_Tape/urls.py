from django.contrib import admin
from django.urls import path
from Ticket_Tape import views

urlpatterns = [
    path("", views.index, name='home'),
    path("account.html", views.account, name='account'),
    path("sent", views.contact, name='contact'),
    path("login", views.login, name='login'),
    path("register", views.register, name='register'),
    path("client.html", views.client, name='client'),
    #path("error.html", views.error, name='error'),
    path("client_profile.html", views.profile, name='profile'),
    path("review.html", views.review1, name='review1'),
    path("review2", views.review2, name='review2'),
    path("edit", views.edit, name='edit'),
    path("search.html", views.search, name='search'),
    path("bookticket", views.bookticket, name='bookticket'),
    path("ticket_pay", views.ticket_pay, name='ticket_pay'),
    path("payment", views.payment, name='payment'),
    path("tickets.html", views.tickets, name='tickets'),
    path("viewticket", views.viewticket, name='viewticket'),
    path("site_admin", views.site_admin, name='site_admin'),
    path("validate_data", views.validate_data, name='validate_data'),
]

