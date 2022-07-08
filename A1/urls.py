from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('about',views.about),
    path('contactus',views.contactus),
    path('book_appointment',views.book_appointment),
    path('patheology',views.patheology),

    path('denstist',views.denstist),
    path('Otolaryngologist',views.Otolaryngologist),
    path('Orthopaedic',views.Orthopaedic),
    path('Neurologist',views.Neurologist),
    path('Gynaecologist',views.Gynaecologist),
    

    # start

    path('form1',views.Form1),
    path('form2',views.Form2),
    path('form3',views.Form3),
    path('form4',views.Form4),
    path('form5',views.Form5),
    path('form6',views.Form6),


]
