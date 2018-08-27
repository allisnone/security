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


def jstest(request):
    data_threat = SECURITY_CONFIG['Security Assessment']['Threat Prevention']
    data_access = SECURITY_CONFIG['Security Assessment']['Access Control']
    data_protection = SECURITY_CONFIG['Data Protection Assessment']['Data Protection']
    
    #print('data=',data)
    return  render(request,'jstest.html',{'data_threat':data_threat,
                                         'data_access':data_access,'data_protection':data_protection})



from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators import csrf
 
# 表单
def search_form(request):
    return render_to_response('search_form.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)



   
# ./polls/views
#http://www.ywnds.com/?p=11834
#https://www.cnblogs.com/pycode/p/upload.html
def upload_file(request):
    # 请求方法为POST时,进行处理;
    if request.method == "POST":
        # 获取上传的文件,如果没有文件,则默认为None;
        File = request.FILES.get("myfile", None)
        if File is None:
            return HttpResponse("no files for upload!")
        else: 
            # 打开特定的文件进行二进制的写操作;
            with open("/tmp/%s" % File.name, 'wb+') as f:
                # 分块写入文件;
                for chunk in File.chunks():
                    f.write(chunk)
            return HttpResponse("upload over!")
    else:
        return render(request, '/upload.html')
    
    
#http://www.cnblogs.com/skyflask/p/9459309.html    
from django.views.decorators.csrf import csrf_exempt

def ajax_get(req):
    return render(req,'ajax_get.html')

@csrf_exempt 
def ajax_post(req):
    if req.method=='POST':
        print(req.POST)
    else:
        print(req.GET)
    return HttpResponse('ajax_post')



def ajax_jsonp(request):
    return render(request,'ajax_cross_success.html')
    #return render(request,'ajax_cross.html')
