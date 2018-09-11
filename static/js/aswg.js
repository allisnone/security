

function aswgSecurityCheck(elementId,dataObj,totalCount){
	/*
	class_para = {ips:"192.168.7.1",ports:"100",contacts:"xiaoxie"};
	dataObj = [
	{
		name:'钓鱼网站访问',
        //urls: "https://api.douban.com/v2/book/search?q=javascript&count=1",
        urls:'http://www.sogaoqing.com/upload/VirusSamples/virus2002',
        detail:'该测试验证您是否可以访问钓鱼网站，来源于 Phishtank.com权威识别的最新钓鱼站点 ',
        description:'待描述',
        method: 'get',
		icon: '../static/images/fail.png',
		cross: '1',
		type: 'jsonp',
		para: '',
    },
	{
		name:'个人隐私信息保护',
        urls: 'add_classes.html',
        detail:'验证是否可以外发保护个人隐私信息 ',
        description:'个人隐私信息包括信用卡号，手机号、中国护照号',
        method: 'post',
		icon: '../static/images/fail.png',
		cross: '0',
		type: 'html',
		para: class_para,
    }
	];
	*/
	statusImg = {
		passed: '../static/images/pass.png',
		failed: '../static/images/fail.png',
	};
	
	if (dataObj.length<1){
		return 0;
	}
	else {
		headDiv = formHeadElement();
		document.getElementById(elementId).appendChild(headDiv);
	}
	var successBlockCount = 0;
	
	for (i=0;i<dataObj.length;i++)
	{
		data = dataObj[i];
		//myUrl = dataObj[i].urls;
		//var patt = new RegExp("http|https");   //判断url是否含有http，https字样
		//alert(patt.test(myUrl));
		//alert('cross site: ' + dataObj[i].cross);
		//alert(dataObj[i].urls);
		//if (patt.test(myUrl)) 
		if (Number(dataObj[i].cross)==1)	//跨站访问
		{
			$.ajax(crossSiteRequest(elementId,data,statusImg));
			//alert('cross site complete: ' + dataObj[i].urls);
		}
		else if (Number(dataObj[i].cross)==2)
		{
			var http_result = 0;
			http_result = xmlhttp(elementId,data,statusImg,totalCount);//(dataObj[i].urls,dataObj[i].para);
			//alert("http_result="+http_result);
			successBlockCount = successBlockCount + http_result;
		}
		else
		{
			$.ajax(internalUlrRequest(elementId,data,statusImg));
			//alert('inter site complete: ' + dataObj[i].urls);
		}
		//sleep(1000);
	}
	return successBlockCount;
	
}

function crossSiteRequest(id,rawData,statusImg){
	dataPara = {};
	if (rawData.method=='post' || rawData.method=='POST') {
		dataPara = {content:rawData.para};
	}
	return {
		type: rawData.method,
        //async: false,
        async: true,
        url: rawData.urls,
        data: dataPara,
        //url: "http://jira.skyguardmis1.com/browse/EI-1055",
        dataType: "jsonp",
        jsonp: "callback",//传递给请求处理程序或页面的，用以获得jsonp回调函数名的参数名(一般默认为:callback)
        jsonpCallback:"flightHandler",//自定义的jsonp回调函数名称，默认为jQuery自动生成的随机函数名，也可以写"?"，jQuery会自动为你处理数据
        success: function(json,textStatus){
			//alert(XMLHttpRequest.status);
            //alert(rawData.name + ' success state cross-site:'+textStatus);
            //if (textStatus == "success") {  //200 ok
              	//document.getElementById(id).innerHTML= id + ' URL: ' + myurl + " :" + 'success' + para1 + para1;
			//	addContentElement(rawData,statusImg)
			//	}
			divItem = addContentElement(rawData,statusImg.failed);
			document.getElementById(id).appendChild(divItem);
            return 1;
        },
        error: function(XMLHttpRequest, textStatus, errorThrown){
            //alert('fail');
            //alert(rawData.name + ' cross fail http code: ' + XMLHttpRequest.status);
            /*
            if (XMLHttpRequest.status == 403) {
           	//document.getElementById(id).innerHTML=id + ' URL: ' + myurl + " :" + XMLHttpRequest.status + para2 + para2;
			divItem = addContentElement(data,statusImg.passed);
			document.getElementById(id).appendChild(divItem);
            }
			else if (XMLHttpRequest.status == 404) {
           	//document.getElementById(id).innerHTML=id + ' URL: ' + myurl + " :" + XMLHttpRequest.status + para2 + para2;
			divItem = addContentElement(data,statusImg.passed);
			document.getElementById(id).appendChild(divItem);
            }
			else {
				alert(XMLHttpRequest.status);
			}
			*/
            divItem = addContentElement(rawData,statusImg.passed);
			document.getElementById(id).appendChild(divItem);
            return 0;
        },
    };
}

function flightHandler(callback){
	alert('callback='+callback);
	
}

function internalUlrRequest(id,rawData,statusImg){
	dataPara = {};
	if (rawData.method=='post' || rawData.method=='POST') {
		dataPara = {content:rawData.para};
	}
	return {
		type:rawData.method,
		url: rawData.urls,
		//async: false,
		data: dataPara,
		//timeout:30000,//30秒
		dataType: rawData.type,//"html",
		success: function(result){
			//alert(data.status);
			//alert(rawData.name + ' inter success data:' + result);
			divItem = addContentElement(rawData,statusImg.failed);
			document.getElementById(id).appendChild(divItem);
            return 1;
        },
        error: function(result,XMLHttpRequest){
			//alert('fail');
            //alert(rawData.name + ' inter fail http code: ' + XMLHttpRequest.status);
            if (XMLHttpRequest.status == 403) {
           	//document.getElementById(id).innerHTML=id + ' URL: ' + myurl + " :" + XMLHttpRequest.status + para2 + para2;
			divItem = addContentElement(rawData,statusImg.passed);
			document.getElementById(id).appendChild(divItem);
            }
			else if (XMLHttpRequest.status == 404) {
           	//document.getElementById(id).innerHTML=id + ' URL: ' + myurl + " :" + XMLHttpRequest.status + para2 + para2;
			divItem = addContentElement(rawData,statusImg.passed);
			document.getElementById(id).appendChild(divItem);
            }
			else {
				//alert(XMLHttpRequest.status);
			}
            return 0; 
		},
	};
}


function addContentElement(data,statusImg){
	var rowDiv = document.createElement("div");
    rowDiv.setAttribute("class","row");
    rowDiv.setAttribute("style","display:flex; background-color:#ffffff;");
    var html = '<div class="col-sm-1">' +
	'<div> <img src="' + statusImg + '" style="width:15px; height:15px; margin:5px;"> </div>' +
	'</div>' +
	'<div class="col-sm-3">' +
	'<p>' + data.name + '</p>' +
	'</div>' +
	'<div class="col-sm-1">' +
	'<div> <img src="' + data.icon + '" style="width:15px; height:15px; margin:5px;"> </div> ' +
	'</div>' +
	'<div class="col-sm-6">' +
	'<p>' +  data.detail + '</p>' +
	'</div>' +
	'<div class="col-sm-1">'
	'<p> </p>' +
	'</div>';
	rowDiv.innerHTML = html;
	return rowDiv;
}


function formHeadElement(){
	var headDiv = document.createElement("div");
	headDiv.setAttribute("class","row");
	var h = '<div class="col-sm-1"> <p> STATUS </p></div>' +
		'<div class="col-sm-3"> <p> TEST NAME </p></div>' +
		'<div class="col-sm-1"> <p> ICON </p></div>' +
		'<div class="col-sm-6"> <p> TEST DETAILS </p></div>' +
		'<div class="col-sm-1"> <p> </p></div>';
	headDiv.innerHTML = h;
	return headDiv;
}


function getHttpObj(){
    var httpobj = null;
    try {
        httpobj = new ActiveXObject("Msxml2.XMLHTTP");
    }
    catch (e) {
        try {
            httpobj = new ActiveXObject("Microsoft.XMLHTTP");
        }
        catch (e1) {
            httpobj = new XMLHttpRequest();
        }
    }
    return httpobj;
 }

function xmlhttp0(id,rawData,statusImg) {
//    var xhr = new XMLHttpRequest();
    var xhr = getHttpObj();
    xhr.open("POST", rawData.urls, true);
    //alert(url+'--test: ' + content);
    xhr.responseType = "text"; //json,document, arraybuffer
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");//缺少这句，后台无法获取参数
    //xhr.setRequestHeader('Content-Type','application/json');
    //alert(url+'--test2: ' + content);
    xhr.onreadystatechange = function(result) {
    	alert("result: " + result);
        
        if (xhr.readyState == 4 && xhr.status == 200) {
        	//alert(url+'--test200: ' + content);
            //console.log("ready: " + xhr.responseText);
            divItem = addContentElement(rawData,statusImg.failed);
			document.getElementById(id).appendChild(divItem);
			alert(rawData.urls +"--test200 : " + "http status4200: " +
					xhr.status + "ready status: " + xhr.readyState + "para: " + rawData.para);
        }
        else if (xhr.readyState == 4 && xhr.status == 0){
        	divItem = addContentElement(rawData,statusImg.passed);
			document.getElementById(id).appendChild(divItem);
			alert(rawData.urls +"--test403 : " + "http status4403: " +
					xhr.status + "ready status: " + xhr.readyState + "para: " + rawData.para);
        }
        else{
        	alert(rawData.urls +"--testother : " + "http status: " +
					xhr.status + "ready status-other: " + xhr.readyState + "para: " + rawData.para);
        }
    };
    var para = {content: rawData.para};
    jspa = JSON.stringify(para);
    try
    {
    	
    	window.onerror = function(errorMessage, scriptURI, lineNumber) {
    		/*
    		 reportError({
    		 message: errorMessage,
    		 script: scriptURI,
    		 line: lineNumber
    		 });
    		 */
    		alert("onerror: " + errorMessage + errorMessage);
    	}
    	xhr.send(jspa);
    	
    }
    catch(err)
    {
    	txt = rawData.urls + 'error: \n\n' + err;
    	alert(txt);
    }
    //xhr.send(para);
      
}


function xmlhttp(id,rawData,statusImg,totalCount) {
//  var xhr = new XMLHttpRequest();
  var resultStatus = 1;
  var xhr = getHttpObj();
  var PassCountDataId ="PassCountData";
  var PassCountSecurityId = "PassCountSecurity";
  var FailCountDataId = "FailCountData";
  var FailCountSecurityId = "FailCountSecurity";
  //xhr.open("POST", rawData.urls, true);
  var url = rawData.urls;
  if (rawData.method =="get" || rawData.method =="GET") {
	  var nowTime = new Date().getTime();//获取当前时间作为随机数
      var url= url + "?time=" +nowTime;
      
      if (rawData.id in [1,2,3,4]) { //解决跨域不可控网站，如恶链/成人/暴力武器/钓鱼网站
    	  url = "/post";
      }
      
  }
  xhr.open(rawData.method, url, true);
  //var totalCount = 21;
  //xhr.setRequestHeader("Cache-Control","no-cache");
  //alert(url+'--test: ' + content);
  if (rawData.method =="post" || rawData.method =="POST"){
	  //xhr.responseType = "text"; //json,document, arraybuffer
	  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");//缺少这句，后台无法获取参;
	  //alert("rawData.method="+"POST");
  }
  //xhr.setRequestHeader('Content-Type','application/json');
  //alert(url+'--test2: ' + content);
  xhr.onreadystatechange = function(result) {
  	  //alert("result: " + result);
      
      if (xhr.readyState == 4 && xhr.status == 200) {
      	//alert(url+'--test200: ' + content);
          //console.log("ready: " + xhr.responseText);
          divItem = addContentElement(rawData,statusImg.failed);
		  document.getElementById(id).appendChild(divItem);
		  if (Number(rawData.id)>=30){
			  updateTestCountResult(FailCountDataId);
		  }
		  else {
			  updateTestCountResult(FailCountSecurityId);
		  }
		  updateProgressBar(totalCount);
		  //alert(rawData.urls +"--test200 : " + "http status4200: " +
					//xhr.status + "ready status: " + xhr.readyState + "para: " + rawData.para);
      }
      else if (xhr.readyState == 4 && xhr.status == 0){
    	  divItem = addContentElement(rawData,statusImg.passed);
		  document.getElementById(id).appendChild(divItem);
		  resultStatus = 1;
		  //var PassCountDataId ="PassCountData";
		  //var PassCountSecurityId = "PassCountSecurity";
		  if (Number(rawData.id)>=30){
			  updateTestCountResult(PassCountDataId);
		  }
		  else {
			  updateTestCountResult(PassCountSecurityId);
		  }
		  updateProgressBar(totalCount);
		  
		  //alert(rawData.urls +"--test403 : " + "http status4403: " +
			//		xhr.status + "ready status: " + xhr.readyState + "para: " + rawData.para);
      }
      else{
      	//alert(rawData.urls +"--testother : " + "http status: " +
					//xhr.status + "ready status-other: " + xhr.readyState + "para: " + rawData.para);
      }
  };
  
  if (rawData.method =="post" || rawData.method =="POST"){
	  var para = {content:" "};
	  if (Number(rawData.id)>=30){ //DLP post
		  para = {content: rawData.para};
	  }
	  var jspa = JSON.stringify(para);
	  //alert("rawData.method="+"POST" +jspa);
	  
	  try
	    {
	    	window.onerror = function(errorMessage, scriptURI, lineNumber) {
	    		/*
	    		 reportError({
	    		 message: errorMessage,
	    		 script: scriptURI,
	    		 line: lineNumber
	    		 });
	    		 */
	    		//alert("onerror: " + errorMessage + errorMessage);
	    	};
	    	xhr.send(jspa);
	    	
	    }
	    catch(err)
	    {
	    	txt = rawData.urls + "error: \n\n" + err;
	    	//alert(txt);
	    }
	  resultStatus = 0;
  }
else if (rawData.method =="get" || rawData.method =="GET"){
	  var para = {content:" "};
	  var text = "www.sogaoqing.com";
	  if (Number(rawData.id)<30 && text.indexOf("sogaoqing")>0){
		  para = {upload:rawData.para};
	  }
	  var jspa = JSON.stringify(para);
	  
	  try
	    {
	    	window.onerror = function(errorMessage, scriptURI, lineNumber) {
	    		/*
	    		 reportError({
	    		 message: errorMessage,
	    		 script: scriptURI,
	    		 line: lineNumber
	    		 });
	    		 */
	    		var a=1;
	    		//alert("onerror: " + errorMessage + errorMessage);
	    	};
	    	xhr.send();
	    	xhr.setRequestHeader("Cache-Control","no-cache");
	    	
	    }
	    catch(err)
	    {
	    	txt = rawData.urls + "error: \n\n" + err;
	    	//alert(txt);
	    }
	  //xhr.send();
	  resultStatus =0;
	  
  }
  else{
	  
	  try
	    {
	    	window.onerror = function(errorMessage, scriptURI, lineNumber) {
	    		/*
	    		 reportError({
	    		 message: errorMessage,
	    		 script: scriptURI,
	    		 line: lineNumber
	    		 });
	    		 */
	    		var a=1;
	    		//alert("onerror: " + errorMessage + errorMessage);
	    	};
	    	xhr.send();
	    	
	    }
	    catch(err)
	    {
	    	txt = rawData.urls + "error: \n\n" + err;
	    	//alert(txt);
	    }
	  //xhr.send();
	  resultStatus =0;
	  
  }
  
  return resultStatus;
    
}
 
function updateTestCountResult(PassCountDataId){
	//var PassCountDataId = "PassCountData";
	var dv = 0;
	dv = document.getElementById(PassCountDataId).innerText;
	//alert("dv=" + dv);
	document.getElementById(PassCountDataId).innerHTML = Number(dv)+1;
	return Number(dv)+1;
}

function updateProgressBar(totalCount){
	var loaderBarId = "loader-bar";
	var loaderInfoId = "loader-info";
	var count = 0;
	var elementIds = ["PassCountData","PassCountSecurity", "FailCountData","FailCountSecurity"];
	for (var i=0;i< elementIds.length;i++){
		//alert(elementIds[i]);
		var currentCount = document.getElementById(elementIds[i]).innerText;
		//alert("currentCount=" + currentCount);
		count = count + Number(currentCount);
	}
	//alert("count="+count);
	var percentage = Number(count/totalCount*100).toFixed(0);
	var pc = percentage + "%";
	//alert(pc);
	var styleStr = "width:" + pc +  ";background-color: #009CDA; height:5px";
	//alert('styleStr='+styleStr);
	//"width:0%;background-color: #009CDA; height:5px"
	var loaderBar = document.getElementById(loaderBarId);
	loaderBar.setAttribute("style", styleStr);
	document.getElementById(loaderInfoId).innerHTML = pc;
	if (percentage==100){
		document.getElementById('loadingBlock').setAttribute("style","display:None");
		var showEmailBlock="border-left: 24px solid #EFEFF0; display:block; background-color:#ffffff;"
		document.getElementById('emailBlock').setAttribute("style",showEmailBlock);
	}
	return pc;
	
}

function sleep(numberMillis) {
	var now = new Date();
	var exitTime = now.getTime() + numberMillis;
	while (true) {
		now = new Date();
		if (now.getTime() > exitTime)
		return;
	    }
}
 
 
 