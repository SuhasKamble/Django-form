from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .models import Form
from django.contrib import messages
# Create your views here.

def form(request):
    if request.method =="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone  = request.POST.get("phone")
        msg = request.POST.get("msg")
        if len(name)<3 or len(email)<3 or len(phone)<10 or len(msg)<3:
            messages.error(request,"Something went wrong,please fil the form correctly.")

        else:
            forms = Form(name=name,email=email,phone=phone,msg=msg)
            forms.save() 
            messages.success(request, 'Form has been successfully submitted!')  

            
        print(name)
    return render(request,"index.html")