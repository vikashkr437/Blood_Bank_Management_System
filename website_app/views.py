from django.shortcuts import render
from django.http import HttpResponse
from website_app.forms import newdonorform, neworderform, newhospitalform
from bloodbank.models import blood, order, bloodbank
from django.db.models import Sum
# Create your views here.


def index(request):
    return render(request,'website_app/index.html')

def home(request):
    return render(request,'website_app/index.html')

def about(request):
    return render(request,'website_app/about.html')

def contact(request):
    bb = bloodbank.objects.all()
    contact = {'name': bb[0].bb_name, 'phone':bb[0].bb_phone_no,'address':bb[0].bb_address, 'email':bb[0].bb_Email}
    return render(request,'website_app/contact.html',{'contact':contact})

def output(request,message1="Thank you for visiting", message2=";)"):
    return render(request,'website_app/output.html',{'message1':message1, 'message2':message2})

def availability(request):
    stocks = {"ap":0,"an":3,"bp":0,"bn":0,"abp":0,"abn":0,"op":0,"on":0}
    stocks['ap'] = blood.objects.filter(bld_type='a+'or'A+').aggregate(Sum('bld_qty'))['bld_qty__sum']
    stocks['bp'] = blood.objects.filter(bld_type='b+'or'B+').aggregate(Sum('bld_qty'))['bld_qty__sum']
    stocks['abp'] = blood.objects.filter(bld_type='ab+'or'AB+'or'Ab+'or'aB+').aggregate(Sum('bld_qty'))['bld_qty__sum']
    stocks['op'] = blood.objects.filter(bld_type='o+'or'O+').aggregate(Sum('bld_qty'))['bld_qty__sum']
    stocks['an'] = blood.objects.filter(bld_type='a-'or'A-').aggregate(Sum('bld_qty'))['bld_qty__sum']
    stocks['bn'] = blood.objects.filter(bld_type='b-'or'B-').aggregate(Sum('bld_qty'))['bld_qty__sum']
    stocks['abn'] = blood.objects.filter(bld_type='ab-'or'AB-'or'Ab-'or'aB-').aggregate(Sum('bld_qty'))['bld_qty__sum']
    stocks['on'] = blood.objects.filter(bld_type='o-'or'O-').aggregate(Sum('bld_qty'))['bld_qty__sum']
    return render(request,'website_app/availability.html', {'stocks':stocks})

def registerdonor(request):
    form = newdonorform()
    if request.method == "POST":
        form = newdonorform(request.POST)

        if form.is_valid():
            form.save(commit=True)
            message1 = "Thank you for registering."
            message2 = "Your registration is successfully completed."
            return output(request,message1,message2)
        else :
            message1 = "Donor Registration Unsucessful!"
            message2 = "ERROR: Form Data Invalid"
            return output(request,message1, message2)

    return render(request,'website_app/registerdonor.html', {'form':form})

def order(request):
    form = neworderform()
    if request.method == "POST":
        form = neworderform(request.POST)

        if form.is_valid():
            bld_typ = form.cleaned_data['bld_typ_req'].upper()
            req_qty = form.cleaned_data['quantity']
            total_stock = blood.objects.filter(bld_typ=bld_typ).aggregate(Sum('bld_qty'))['bld_qty__sum']
            stock_used = order.objects.filter(bld_typ_req=bld_typ).aggregate(Sum('quantity'))['quantity__sum']
            remaining_stock = total_stock - stock_used
            if req_qty <= remaining_stock :
                form.save(commit=True)
                message1 = "Thank you for registering."
                message2 = "Your registration is successfully completed."
                return output(request,message1,message2)
            else :
                message1 = "Order could not be placed!"
                message2 = "Required Blood Quantity Unavailable"
                return output(request,message1, message2)
        else :
            message1 = "Order could not be placed!"
            message2 = "ERROR: Form Data Invalid"
            return output(request,message1, message2)

    return render(request,'website_app/order.html', {'form':form})


def registerhospital(request):
    form = newhospitalform()
    if request.method == "POST":
        form = newhospitalform(request.POST)

        if form.is_valid():
            form.save(commit=True)
            message1 = "Thank you for registering your hospital."
            message2 = "Your hospital registration is successfully completed."
            return output(request,message1,message2)
        else :
            message1 = "Hospital Registration Unsucessful!"
            message2 = "ERROR: Form Data Invalid"
            return output(request,message1, message2)

    return render(request,'website_app/registerhospital.html', {'form':form})