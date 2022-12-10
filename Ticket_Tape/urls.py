from django.contrib import admin
from django.urls import path
from Ticket_Tape import views

urlpatterns = [
    path("", views.index, name='home'),
    path("contact_success", views.index, name='contact_success'),
    path("home", views.index, name='home'),
    path("account.html", views.account, name='account'),
    path("sent", views.contact, name='contact'),
    path("login", views.login, name='login'),
    path("register", views.register, name='register'),
    path("client.html", views.client, name='client'),
    path("error1", views.error1, name='error1'),
    path("error2", views.error2, name='error2'),
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
    path("site_admin_login", views.siteadminlogin, name='siteadminlogin'),
    path("contact_form_error", views.contact, name='contact_form_error'),
    path("contact_form_success", views.contact, name='contact_form_success'),
    path("siteadminsignin", views.siteadminsignin, name='siteadminsignin'),
]

