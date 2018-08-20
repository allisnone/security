from django.shortcuts import render,redirect
from . import models
from aiohttp.client import request
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

def logout(request):
    return redirect('logout.html')

def index(request):
    return redirect('/index.html')