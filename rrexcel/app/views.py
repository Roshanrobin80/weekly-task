from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def rrhome(req):
    return render(req,'home.html')

def contact(req):
    if req.method=='POST':
        name=req.POST['name']
        phone=req.POST['phone']
        email=req.POST['email']
        msg=req.POST['msg']
        data=cnt.objects.create(name=name,email=email,phone=phone,msg=msg)
        data.save()
        return redirect(contact)
    return render(req,'contact.html')