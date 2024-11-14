from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import *
from django.contrib import messages
from .models import *
import os


# Create your views here.

def shop_login(req):
    if 'pets' in req.session:
        return redirect(shop_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['pswd']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            req.session['pets']=uname   #create session
            return redirect(shop_home)
        else:
            messages.warning(req,"please check your username or password")
            return render(req,'login.html')
    
    else:
        return render(req,'login.html')
    
def shop_logout(req):
    req.session.flush()          #delete session
    logout(req)
    return redirect(shop_login)

def shop_home(req):
    if 'pets' in req.session:
        data=Pets.objects.all()
        return render(req,'shop/home.html',{'pets':data})
    else:
        return redirect(shop_login)

def add_pet(req):
    if 'pets' in req.session:
        if req.method=='POST':
            pet_id=req.POST['pet_id']
            pet_type=req.POST['pet_type']
            pet_breed=req.POST['pet_breed']
            pet_price=req.POST['pet_price']
            offer_price=req.POST['offer_price']
            img=req.FILES['img']
            dis=req.POST['dis']
            data=Pets.objects.create(pet_id=pet_id,pet_type=pet_type,pet_breed=pet_breed,pet_price=pet_price,offer_price=offer_price,img=img,dis=dis)
            data.save()
            return redirect(add_pet)
        else:
            return render(req,'shop/add_pet.html')
    else:
        return redirect(shop_login)

def edit_pet(req,pid):
    if 'pets' in req.session:
        if req.method=='POST':
            pet_id=req.POST['pet_id']
            pet_type=req.POST['pet_type']
            pet_breed=req.POST['pet_breed']
            pet_price=req.POST['pet_price']
            offer_price=req.POST['offer_price']
            img=req.FILES['img']
            dis=req.POST['dis']
            if img:
                Pets.objects.filter(pk=pid).update(pet_id=pet_id,pet_type=pet_type,pet_breed=pet_breed,pet_price=pet_price,offer_price=offer_price,img=img,dis=dis)
                data=Pets.objects.get(pk=pid)
                data.img=img
                data.save()
            else:
                Pets.objects.filter(pk=pid).update(pet_id=pet_id,pet_type=pet_type,pet_breed=pet_breed,pet_price=pet_price,offer_price=offer_price,img=img,dis=dis)
            return redirect(shop_home)
        else:
            data=Pets.objects.get(pk=pid)
            return render(req,'seller/edit.html',{'product':data})
    else:
        return redirect(shop_login) 

# def dlt_bk(req,pid):
#     data=Books.objects.get(pk=pid)
#     url=data.img.url
#     og_path=url.split('/')[-1]
#     os.remove('media/'+og_path)
#     data.delete()
#     return redirect(seller_home) 



