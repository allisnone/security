# -*- coding:utf-8 -*-
from django.shortcuts import render,redirect,reverse
from . import models
from aiohttp.client import request
from aswg.config import SECURITY_CONFIG,URL_MAPPING,PROXIES,IMAGE_STATUS
import json
import datetime,time

from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden
from django.shortcuts import render_to_response
#from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
import os
from django.core import serializers
from django.template import RequestContext
# Create your views here.

from aswg.url_request import get_request,post_request,http_request

def home(request):
    return render(request, 'home.html')

def crosshttp(request,method_id):
    proxy = {}
    remote_addr =''
    try:
        print(request.META['HTTP_ORIGIN'])
        print(type(request.META['REMOTE_ADDR']))
        remote_addr = str(request.META['REMOTE_ADDR'])
        
        if '49.4.84.41' in remote_addr:
            proxy = {'http': 'http://49.4.84.41:8066'}
    except:
        pass
        print('remote_addr --- except')
    print("remote_addr:",remote_addr)
    print(request.META['REMOTE_ADDR'])
    print('proxy=',proxy)
    data_threat = SECURITY_CONFIG['Security Assessment']['Threat Prevention']
    data_access = SECURITY_CONFIG['Security Assessment']['Access Control']
    data_protection = SECURITY_CONFIG['Data Protection Assessment']['Data Protection']
    print('method_id=',URL_MAPPING[method_id])
    url_data = URL_MAPPING[method_id]
    #result = http_request(url_data['urls'],type=url_data['method'],uri='',data={'content':url_data['para']},headers={},proxy=PROXIES)
    #result = get_request(url_data['urls'],proxy=proxy)
    result = http_request(url_data['urls'],params=url_data['para'],type=url_data['method'],headers={},proxy=proxy)
    #return HttpResponse('content=')
    print('result=',result,'proxy=', proxy)
    formid ='urlform%s'%method_id
    status_imge = IMAGE_STATUS['fail']
    #print(type(result[2]))
    if result[2]==403:
        status_imge = IMAGE_STATUS['pass']
        data = {'result':result[3],'icon':URL_MAPPING[method_id]['icon'],'status_img':status_imge}
        data_dict = {formid:json.dumps(result)}
        return HttpResponseForbidden()
    data = {'result':result[3],'icon':URL_MAPPING[method_id]['icon'],'status_img':status_imge}
    data_dict = {formid:json.dumps(result)}
    return HttpResponse()#'content='+url_data['para'])
    #return HttpResponseRedirect('/load',data_dict)#reverse('index'))
    
    #render_to_response("index.html", locals(),context_instance=RequestContext(request))

def base(request):
    return render(request,'index.html')
    #return render(request,'zscaler.html')

def get_classes(request):
    portlists=models.chkportinfo.objects.all()
    return render(request,'get_classes.html',{'portlists':portlists})

@csrf_exempt 
def add_classes(request):
    if request.method == "GET":
        return render(request, 'add_classes.html')
    elif request.method == 'POST':
        #print(request.POST)
        ips = request.POST.get('ips')
        ports=request.POST.get('ports')
        contacts=request.POST.get('contacts')
        #print(ips)
        #print(contacts)
        models.chkportinfo.objects.create(ips=ips,ports=ports,contact=contacts)
        return redirect('get_classes.html')
    
def post_classes(request):
    ips = request.POST.get('ips')
    ports = request.POST.get('ports')
    contacts = request.POST.get('contacts')
    models.chkportinfo.objects.create(ips=ips,ports=ports,contact=contacts)
    return HttpResponse()
 
def del_classes(request):
    id = request.GET.get('id')
    models.chkportinfo.objects.filter(id=id).delete()
    return redirect('get_classes.html')
 
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
        models.chkportinfo.objects.filter(id=id).update(ips=ips,ports=ports,contact=contacts)
        return redirect('get_classes.html')

def login(request):
    return redirect('login.html')

@csrf_exempt
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


def ajax_get(req):
    return render(req,'ajax_get.html')

@csrf_exempt 
def ajax_post(req):
    if req.method=='POST':
        print(req.POST)
    else:
        print(req.GET)
    data_threat = SECURITY_CONFIG['Security Assessment']['Threat Prevention']
    data_access = SECURITY_CONFIG['Security Assessment']['Access Control']
    data_protection = SECURITY_CONFIG['Data Protection Assessment']['Data Protection']
    #print('data_threat',data_threat)
    #data_threat = json.load(data_threat)#serializers('json',data_threat)
    #data_access = json.load(data_access)#serializers('json',data_access)
    #data_protection = json.load(data_protection)#serializers('json',data_protection)
    
    data_dict = {'data_threat':json.dumps(data_threat),'data_access':json.dumps(data_access),'data_protection':json.dumps(data_protection)}
    response = HttpResponse(data_dict)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


@csrf_exempt
def ajax_jsonp(request):
    print(request.META)
    data_threat = SECURITY_CONFIG['Security Assessment']['Threat Prevention']
    data_access = SECURITY_CONFIG['Security Assessment']['Access Control']
    data_protection = SECURITY_CONFIG['Data Protection Assessment']['Data Protection']
    #print('data_threat',data_threat)
    now_time = datetime.datetime.now().strftime('%A %Y-%m-%d %H:%M:%S %p')
    #data_threat = json.load(data_threat)#serializers('json',data_threat)
    #data_access = json.load(data_access)#serializers('json',data_access)
    #data_protection = json.load(data_protection)#serializers('json',data_protection)
    
    data_dict = {'data_threat':json.dumps(data_threat),'data_access':json.dumps(data_access),
                 'data_protection':json.dumps(data_protection),'now_time':now_time}
    #raw_data = json.load(data_dict)
    #json_data = json.dumps(data_dict)#({'rawData':data_dict})
    #print('data=',data)
    #Access-Control-Allow-Headers:x-requested-with
    #response = render_to_response('ajax_cross_success.html',data_dict,context_instance=RequestContext(request))
    #response["Access-Control-Allow-Headers"] = "*"
    print(request.method)
    #print('META.REMOTE_HOST:',request.META['REMOTE_HOST'])
    #time.sleep(2);
    if request.method=='GET':
        return  render(request,'ajax_cross_success.html',data_dict)
    elif request.method=='OPTIONS':
        response = HttpResponse(data_dict)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
    elif request.method=='POST':
        response = HttpResponse(data_dict)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        print('reponse cros post')
        return response
    return  render(request,'ajax_cross_success.html',data_dict)
    #return render(request,'ajax_cross_success.html')
    #return render(request,'ajax_cross_success.html')
    #return render(request,'ajax_cross.html')
    
    #response = HttpResponse(json.dumps({"key": "value", "key2": "value"}))
    #response["Access-Control-Allow-Origin"] = "*"
    #response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    #response["Access-Control-Max-Age"] = "1000"
    #response["Access-Control-Allow-Headers"] = "*"
    
    
@csrf_exempt    
def params_post(request):
    BASE_DIR = 'D:/upload/'
    if request.method=='GET':
        return render(request,'post.html')
    else:
        myFile = request.FILES.get("file", None)
        if myFile:
            destination = open(os.path.join(BASE_DIR, myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
            for chunk in myFile.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()
            return HttpResponse('file='+myFile.name)
        content=request.POST.get('content','')
        print('content=',content)
        #password=request.POST.get('password','')
        return HttpResponse('content='+content)#+"&password="+password)
