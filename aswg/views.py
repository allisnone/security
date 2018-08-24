# -*- coding:utf-8 -*-
from django.shortcuts import render,redirect
from . import models
from aiohttp.client import request
from aswg.config import SECURITY_CONFIG
import json
# Create your views here.

def base(request):
    return render(request,'index.html')
    #return render(request,'zscaler.html')

def get_classes(request):
    portlists=models.chkportinfo.objects.all()
    return render(request,'get_classes.html',{'portlists':portlists})
 
def add_classes(request):
    if request.method == "GET":
        return render(request, 'add_classes.html')
    elif request.method == 'POST':
        ips = request.POST.get('ips')
        ports=request.POST.get('ports')
        contacts=request.POST.get('contacts')
        models.chkportinfo.objects.create(IPs=ips,ports=ports,contact=contacts)
        return redirect('/get_classes.html')
 
 
def del_classes(request):
    id = request.GET.get('id')
    models.chkportinfo.objects.filter(id=id).delete()
    return redirect('/get_classes.html')
 
def edit_classes(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        obj = models.chkportinfo.objects.filter(id=id).first()
        return render(request, 'edit_classes.html', {'obj': obj})
    elif request.method == 'POST':
        id = request.GET.get('id')
        ips = request.POST.get('ips')
        ports = request.POST.get('ports')
        contacts=request.POST.get('contacts')
        models.chkportinfo.objects.filter(id=id).update(IPs=ips,ports=ports,contact=contacts)
        return redirect('/get_classes.html')

def login(request):
    return redirect('login.html')


def loading(request):
    data_threat = SECURITY_CONFIG['Security Assessment']['Threat Prevention']
    data_access = SECURITY_CONFIG['Security Assessment']['Access Control']
    data_protection = SECURITY_CONFIG['Data Protection Assessment']['Data Protection']
    #print('data=',data)
    return  render(request,'index.html',{'data_threat':data_threat,
                                         'data_access':data_access,'data_protection':data_protection})

def logout(request):
    return redirect('logout.html')

def index(request):
    return redirect('/index.html')