from django.shortcuts import render
import requests
import datetime
from A1.models import *

def home(request):
    return render(request, 'home.html')

 
def about(request):
    return render(request, 'about.html')
    
 
def contactus(request):
    return render(request, 'contactus.html')


def book_appointment(request):
    return render(request,'signup.html')


def patheology(request):
    return render(request,'patheology.html')


def denstist(request):
    return render(request,'denstist.html')


def Otolaryngologist(request):
    return render(request,'Otolaryngologist.html')


def Orthopaedic(request):
    return render(request,'Orthopaedic.html')


def Neurologist(request):
    return render(request,'neurologist.html')


def Gynaecologist(request):
    return render(request,'Gynaecologist.html')
def login(request): 
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password'] 

        context = {'msg' : "wrong"}
        if user_data.objects.filter(user_name = username,password = password)[0] is None :
            return render(request,'login.html',context)

        return render(request,'book_appointment.html')
    return render(request,'login.html')

def Form1(request):
    if request.method=='POST':
        name=request.POST['name']
        contact=request.POST['contact']
        symptom=request.POST['symptom']
        date=request.POST['date']
        time=request.POST['time']
        doctor=request.POST['doctor']
        form1_data(patient_name=name,patient_mob_no=contact,patient_desiese_symptom=symptom,date=date,time=time,curr_date_time=datetime.datetime.now()).save()
        return render(request,'form1.html',{'msg':" We will connect you soon"})
    return render(request,'form1.html')

    # 2nd

def Form2(request):
    if request.method=='POST':
        name=request.POST['name']
        contact=request.POST['contact']
        symptom=request.POST['symptom']
        date=request.POST['date']
        time=request.POST['time']
        doctor=request.POST['doctor']
        form2_data(patient_name=name,patient_mob_no=contact,patient_desiese_symptom=symptom,date=date,time=time,curr_date_time=datetime.datetime.now()).save()
        return render(request,'form2.html',{'msg':" We will connect you soon"})
    return render(request,'form2.html')

def Form3(request):
    if request.method=='POST':
        name=request.POST['name']
        contact=request.POST['contact']
        symptom=request.POST['symptom']
        date=request.POST['date']
        time=request.POST['time']
        doctor=request.POST['doctor']
        form3_data(patient_name=name,patient_mob_no=contact,patient_desiese_symptom=symptom,date=date,time=time,curr_date_time=datetime.datetime.now()).save()
        return render(request,'form3.html',{'msg':" We will connect you soon"})
    return render(request,'form3.html')

def Form4(request):
    if request.method=='POST':
        name=request.POST['name']
        contact=request.POST['contact']
        symptom=request.POST['symptom']
        date=request.POST['date']
        time=request.POST['time']
        doctor=request.POST['doctor']
        form4_data(patient_name=name,patient_mob_no=contact,patient_desiese_symptom=symptom,date=date,time=time,curr_date_time=datetime.datetime.now()).save()
        return render(request,'form4.html',{'msg':" We will connect you soon"})
    return render(request,'form4.html')

def Form5(request):
    if request.method=='POST':
        name=request.POST['name']
        contact=request.POST['contact']
        symptom=request.POST['symptom']
        date=request.POST['date']
        time=request.POST['time']
        doctor=request.POST['doctor']
        form5_data(patient_name=name,patient_mob_no=contact,patient_desiese_symptom=symptom,date=date,time=time,curr_date_time=datetime.datetime.now()).save()
        return render(request,'form5.html',{'msg':" We will connect you soon"})
    return render(request,'form5.html')

def Form6(request):
    if request.method=='POST':
        name=request.POST['name']
        contact=request.POST['contact']
        symptom=request.POST['symptom']
        date=request.POST['date']
        time=request.POST['time']
        doctor=request.POST['doctor']
        form6_data(patient_name=name,patient_mob_no=contact,patient_desiese_symptom=symptom,date=date,time=time,curr_date_time=datetime.datetime.now()).save()
        return render(request,'form6.html',{'msg':" We will connect you soon"})
    return render(request,'form6.html')                
    
def sign_up(request):
    if request.method == 'POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        # return render(request,"jjk",msg1)
        
        # if user_data.objects.filter(user_name = username) is not None :
        #     return render(request,"signup.html",{'msg' : "username exists"})

        user_data(name=name,user_name=username,email=email,password=password ).save()
    return render(request,'signup.html',{'msg' : "username siccess"})
