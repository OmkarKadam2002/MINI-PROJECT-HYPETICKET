from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from Ticketing_Website import settings
from .models import Destination, Account,Review, Monument, Tickets
from django.contrib import messages
from django.conf import settings
import stripe
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.


def index(request):
    return render(request, 'index.html')
def tickets(request):
    username=request.session.get('username')
    mydata = Tickets.objects.filter(username=username).values()
    return render(request, 'tickets.html',{'mymembers' : mydata})
def viewticket(request):
    username=request.session.get('username')
    mydata = Tickets.objects.filter(username=username).values()
    return render(request, 'viewticket.html',{'mymembers' : mydata})
def account(request):
    return render(request, 'account.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']
        error_message = None
        success_message = None
        if(not name):
            error_message = "Name Required."
        elif len(name) < 2:
            error_message = "Name Cannot be a single letter."
        elif(not email):
            error_message = "Email Required."
        elif("@" not in email):
            error_message = "Enter a valid Email."
        elif(not number):
            error_message = "Number Required."
        elif len(number) < 10:
            error_message = "Enter a valid Number."
        elif(not message):
            error_message = "Message Cannot be empty"
        if not error_message:
            success_message = "Message Has been Sent SuccessFully."
            contact= Destination(name=name, email_id=email,number=number, message=message)
            contact.save()
            return render(request, 'index.html', {'success' : success_message})
        else:
            return render(request, 'index.html', {'error' : error_message})
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        request.session['username']=username
        password = request.POST.get('password')
        a = False
        b = False
        loginerror=None
        for username in Account.objects.all():
            a = True
        for password in Account.objects.all():
            b = True
        if a & b == True :
            return redirect('client.html') 
        else:
            loginerror = "Invalid Username or Password"
            return render(request, 'error.html', {'login_error' : loginerror})
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        error_message = None
        if(not name):
            error_message = "Name Required."
        elif len(name) < 2:
            error_message = "Name Cannot be a single letter."
        elif(not email):
            error_message = "Email Required."
        elif("@" not in email):
            error_message = "Enter a valid Email."
        elif(not username):
            error_message = "Username Required."
        elif len(username) < 8:
            error_message = "Username needs to be of minimum 8 characters."
        elif(not password or not conpassword):
            error_message = "Password Required."
        elif len(password) < 8 or len(conpassword) < 8:
            error_message = "Password needs to be of minimum 8 characters."
        elif(password != conpassword):
            error_message = "Passwords Do not Match."
        if not error_message:
            request.session['username']=username
            register = Account(name=name, email_id=email,username=username,password=password,conpassword=conpassword)
            register.save()
            return redirect('client.html')   
        else:
            return render(request, 'error.html', {'error' : error_message})
def client(request):
    return render(request, 'client.html') 
def payment(request):
    if request.method == 'POST':
        price=request.session.get('price')
        charge = stripe.PaymentIntent.create(
            amount=price,
            currency='inr',
            description='Payment Gateway',
        )
        username=request.session.get('username')
        print(username)
        name = Account.objects.values_list('name', flat=True).get(username=username)
        email = Account.objects.values_list('email_id', flat=True).get(username=username)
        number = Account.objects.values_list('number', flat=True).get(username=username)
        count_ind=request.session.get('count_ind')
        count_for=request.session.get('count_for')
        count_free=request.session.get('count_free')
        date=request.session.get('date')
        monument_name=request.session.get('monument_name')
        location = Monument.objects.values_list('location', flat=True).get(name=monument_name)
        count_ind1=str(count_ind)
        count_for1=str(count_for)
        count_free1=str(count_free)
        price1=str(price)
        part1=name+" "+email+" "+number+" "+monument_name+" "+location+" "+date
        part2=count_ind1+" "+count_for1+" "+count_free1+" "+price1
        part3=part1+" "+part2
        """qrcode_img = qrcode.make(part3)
        canvas = Image.new('RGB',(290,290),'white')
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname=f'qr_code-{date}.png'
        buffer=BytesIO()
        canvas.save(buffer,'PNG')
        qrcode_img.save(fname, File(buffer),save=False)
        canvas.close()"""
        ticket_save = Tickets(name=name,email_id=email,number=number,date=date,monument_name=monument_name,location=location,count_ind=count_ind,count_for=count_for,count_free=count_free,price=price,username=username)
        ticket_save.save()
        return render(request, 'payment_successful.html') 
def bookticket(request):
    if request.method == 'POST':   
        val = request.POST['bookticketbutton']
        mydata = Monument.objects.filter(id=val).values()
        monument_name = Monument.objects.values_list('name', flat=True).get(id=val)
        request.session['monument_name']=monument_name
    return render(request, 'bookticket.html', {'mymembers' : mydata })  
def search(request):
    return render(request, 'search.html')  
def ticket_pay(request):
    if request.method == 'POST':
        date=request.POST['date_booked']
        price_ind=request.POST['price_ind']
        price_for=request.POST['price_for']
        price_free=request.POST['price_free']
        count_ind=request.POST['count_ind']
        count_for=request.POST['count_for']
        count_free=request.POST['count_free']
        ind=int(price_ind)
        forn=int(price_for)
        cind=int(count_ind)
        cforn=int(count_for)
        price=(ind*cind)+(forn*cforn)
        request.session['count_ind']=count_ind
        request.session['count_for']=count_for
        request.session['count_free']=count_free
        request.session['date']=date
        request.session['price']=price
        key=settings.STRIPE_PUBLISHABLE_KEY
        return render(request, 'Payment.html',{'price': price})  
def profile(request):
    username=request.session.get('username')
    #mydata = Account.objects.values_list('name', flat=True).get(username=username)
    mydata = Account.objects.filter(username=username).values()
    print(mydata)
    return render(request, 'client_profile.html', {'mymembers': mydata})
def validate_data(request):
    if request.method == 'POST':
        string_data = request.POST['ticket_data']
        print(string_data)
        return HttpResponse("heyo")
def edit(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        username = request.POST['username']
        age = request.POST['age']
        email = request.POST['email']
        location = request.POST['location']
        Account.objects.filter(username=username).update(name=name, email_id=email,username=username,number=number,age=age,location=location)
        mydata = Account.objects.filter(username=username).values()
        return render(request, 'client_profile.html',{'mymembers': mydata})
def review1(request):
    username=request.session.get('username')
    mydata = Review.objects.filter(username=username).values()
    return render(request, 'review.html',{'mymembers': mydata})  
def review2(request):
    if request.method == 'POST':
        username=request.session.get('username')
        name = Account.objects.values_list('name', flat=True).get(username=username)
        location = Account.objects.values_list('location', flat=True).get(username=username)
        rating=request.POST['rating']
        review=request.POST['reviews']
        if username in Review.objects.all():
            Review.objects.filter(username=username).update(username=username,name=name,review=review,rating=rating,location=location)
        else:
            review_save = Review(username=username,name=name,review=review,rating=rating,location=location)
            review_save.save()
        return render(request, 'review.html')  
def site_admin(request):
    return render(request, 'site_admin.html')



