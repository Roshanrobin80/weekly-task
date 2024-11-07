from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .models import *
from . import views
import os
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['pswd']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['shop']=uname
                return redirect(shop_home)
            else:
                login(req,data)
                req.session['user']=uname
                return redirect(user_home)
        else:
            messages.warning(req,"invalid username or password")
            return redirect(shop_login)
    else:
        return render(req,'login.html')
    
def shop_logout(req):
    req.session.flush()
    logout(req)
    return redirect(shop_login)



