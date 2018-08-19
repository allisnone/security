//use to set Menu active
function SetMenuActive(menuUrl){
	var urlstr = location.href;
	var urlstatus=false;
	$("#menu li").each(function () {
		if ($(this).attr('value')== menuUrl ) {
			$(this).addClass('active'); urlstatus = true;
		} else {
			$(this).removeClass('active');
		}
	});
	if (!urlstatus) {$("#menu li a").eq(0).addClass('active');}
};

function getUrl(menuURL,siteid) {
    var url = menuURL + '?siteid=' + siteid;
    return url;
};

//use to set URL for report page
function getReportUrl(reportType){
	var reportUrl = "/report/";
	var mydateend = new Date();
	var mydatestart = new Date();
	mydatestart.setTime(mydateend.getTime()-7*24*60*60*1000);
	var enddate = (mydateend.getMonth()+1)+"/"+mydateend.getDate()+"/"+mydateend.getFullYear();
	var startdate = (mydatestart.getMonth()+1)+"/"+mydatestart.getDate()+"/"+mydatestart.getFullYear();
	var siteId = $('#treeview').jstree().get_selected();
	var transUrl = getUrl(reportUrl,siteId) + '&type=' + reportType + '&sdate=' + startdate + '&edate='+enddate;
	return transUrl;
};

//use to show loading picture for report page
function ShowLoading(){
	$('#myModal').modal('show');
	// For IE, need to reload the gif image with multiple frames
	var navigatorName = "Microsoft Internet Explorer";
	if (navigator.appName == navigatorName){
		$("#loading").css("background","transparent url('../../static/img/ajax-loader1.gif') 50% 50% no-repeat");
	}
};
//use to hide loading picture for report page
function HideLoading(){
	$('#myModal').modal('hide');

};

//use to set alarm table
function initTable(element, data){
	this.$element = $(element);
	return this.$element.DataTable({
        "data": data.tableData,
        "columns": data.fieldData,
 		"aaSorting" : [[0,'desc']],	//make the first colume desc order
		"bJQueryUI": true,
		"pagingType": "full_numbers",
		destroy: true,
	});
}
//use to set alarm table
function setAlarmTable(data){
	var oTable = initTable("#alarmtable", data)

	oTable.search('activate');
	oTable.$('tr', {search: "applied"}).css('backgroundColor', '#f2dede');
	oTable.search('');
};

//use to set default Chart options
function defaultData(Options){

	// define the basic Option for DC Load Rate Bar Chart.
	Options = {
			title : {
				textStyle : {
					fontSize : 12
				},
			},
			tooltip : {
				trigger : 'axis'
			},
			legend : {
				data : [ '' ]
			},
			toolbox : {
				show : true,
				feature : {
					mark : {
						show : false
					},
					dataView : {
						show : false,
						readOnly : false
					},
					magicType : {
						show : true,
						type : [ 'line', 'bar' ],
						title:{
							line:'line',
							bar:'bar'
						}

					},
					restore : {
						show : false,
						title:'restore'
					},
					saveAsImage : {
						show : true,
						title:'save'
						
					}
				}
			},
			calculable : true,
			grid : {
				x : 50,
				y : 40,
				x2 : 40,
				y2 : 50
			},
			xAxis : [ {
				type : 'category',
				scale: true,
				//adjust the label
				axisLabel : {
					show : true,
					//rotate: 30,
					textStyle : {
						fontSize : 10
					}
				}
			} ],
			yAxis : [ {
				type : 'value',
				scale: true,
				splitArea : {
					show : true
				}
			} ],
			series : [ {
				type : 'bar',
			} ],
	};

	return Options;
};

//use to set Chart data for day/week/month/quarter/year
function reloadbase(datetype, data, charName){
	var p = charName.getOption();
	
	switch(datetype){
	case 'week':
		p.series[0].data = data.Ydata.week;
		p.xAxis[0].data = data.Xdata.week;
		break;
	case 'month':
		p.series[0].data = data.Ydata.month;
		p.xAxis[0].data = data.Xdata.month;
		break;
	case 'quarter':
		p.series[0].data = data.Ydata.quarter;
		p.xAxis[0].data = data.Xdata.quarter;
		break;
	case 'year':
		p.series[0].data = data.Ydata.year;
		p.xAxis[0].data = data.Xdata.year;
		break;
	default:
		//day
		p.series[0].data = data.Ydata.day;
		p.xAxis[0].data = data.Xdata.day;
		break;
	};
	
	charName.setOption(p,true); 
};


function setChart(option, data, chartElement, divElement, textList, chartName){
	option = defaultData(option);
	option.yAxis[0].name = textList[0];
	option.series[0].name = textList[1];
	option.series[0].data = data.default[0].yArray_data;
	option.xAxis[0].data = data.Xdata[data.default[0].datetype];

	chartName = echarts.init(document.getElementById(chartElement));
	chartName.setOption(option,true);
	$(divElement).children("button").click(function(){
		reloadbase($(this).val(), data, chartName);
	});
};

//use to set DC Efficiency Chart
function setDCEffChart(data){
	var tempDC_Eff = data;

	var DC_EffOption = '';
	DC_EffOption = defaultData(DC_EffOption);
	DC_EffOption.yAxis[0].name = "%";
	DC_EffOption.series[0].name = 'DC Efficiency';
	DC_EffOption.series[0].data = tempDC_Eff.default[0].yArray_data;
	DC_EffOption.xAxis[0].data = tempDC_Eff.Xdata[tempDC_Eff.default[0].datetype];

	DC_EffchartName = echarts.init(document.getElementById('DCefficiency'));
	DC_EffchartName.setOption(DC_EffOption);

	$("#dc_eff_div > button").click(
		function(){
			reloadbase($(this).val(), tempDC_Eff, DC_EffchartName);
	});
};
//use to set AD Efficiency Chart
function setADEffChart(data){
	var tempAD = data;

	var ADOption = '';
	ADOption = defaultData(ADOption);
	ADOption.series[0].name = 'AD Efficiency';
	ADOption.yAxis[0].name = "%";
	ADOption.series[0].data = tempAD.default[0].yArray_data;
	ADOption.xAxis[0].data = tempAD.Xdata[tempAD.default[0].datetype];

	ADchartName = echarts.init(document.getElementById('ADefficiency'));
	ADchartName.setOption(ADOption);

	$("#ad_eff_div > button").click(
		function(){
			reloadbase($(this).val(), tempAD, ADchartName);
	});
};
//use to set DC Load Chart

function setDCLoadChart(data){
	var tempDC_Load = data;

	var DC_LoadOption = '';
	DC_LoadOption = defaultData(DC_LoadOption);
	DC_LoadOption.yAxis[0].name = "%";
	DC_LoadOption.series[0].name = 'DC Load Rate';
	DC_LoadOption.series[0].data = tempDC_Load.default[0].yArray_data;
	DC_LoadOption.xAxis[0].data = tempDC_Load.Xdata[tempDC_Load.default[0].datetype];

	DC_LoadchartName = echarts.init(document.getElementById('DCloadrate'));
	DC_LoadchartName.setOption(DC_LoadOption);

	$("#dc_load_div > button").click(
		function(){
			reloadbase($(this).val(), tempDC_Load, DC_LoadchartName);
	})
};
//use to set TC Chart
function setTCChart(data){
	var tempTC = data;

	var TCOption = '';
	TCOption = defaultData(TCOption);
	TCOption.yAxis[0].name = "kWh";
	TCOption.series[0].name = 'Total Consumption';
	TCOption.series[0].data = tempTC.default[0].yArray_data;
	TCOption.xAxis[0].data = tempTC.Xdata[tempTC.default[0].datetype];

	TCchartName = echarts.init(document.getElementById('TotalConsumption'));
	TCchartName.setOption(TCOption);

	$("#tc_div > button").click(
		function(){
			reloadbase($(this).val(), tempTC, TCchartName);
	});
};

//use to set PUE Chart
function setPUEChart(data){
	var tempPUE = data;
	var PUEOption = '';
	PUEOption = defaultData(PUEOption);
	PUEOption.series[0].name = 'Site PUE';
	PUEOption.series[0].data = tempPUE.default[0].yArray_data;
	PUEOption.series[0].type='line';
	PUEOption.xAxis[0].data = tempPUE.Xdata[tempPUE.default[1].datetype];
	PUEchartName = echarts.init(document.getElementById('pueReport'));
	PUEchartName.setOption(PUEOption);
	var markdata={
			data:[
			      {type:'min',name:'Min'},
			      {type:'max',name:'Max'}
			      ]
	};
	PUEchartName.addMarkPoint(0,markdata);  //0-for series[0]

	$("#pue_div > button").click(
		function(){
			reloadbase($(this).val(), tempPUE, PUEchartName);
	});
};

//use to set UPS Efficiency Chart
function setUPSEffChart(data){
	var tempUpseff = data;
	var UPSEffOption = '';
	UPSEffOption = defaultData(UPSEffOption);
	UPSEffOption.yAxis[0].name = "%";
	UPSEffOption.series[0].name = 'UPS Efficiency';
	UPSEffOption.series[0].data = tempUpseff.default[0].yArray_data;
	UPSEffOption.series[0].type='line';
	UPSEffOption.xAxis[0].data = tempUpseff.Xdata[tempUpseff.default[1].datetype];
	UPSEffchartName = echarts.init(document.getElementById('upseffReport'));
	UPSEffchartName.setOption(UPSEffOption);

	$("#upseff_div > button").click(
		function(){
			reloadbase($(this).val(), tempUpseff, UPSEffchartName);
	});
};


//use to set UPS Load Chart
function setUPSLoadChart(data){
	var tempUpsload = data;
	var UPSLoadOption = '';
	UPSLoadOption = defaultData(UPSLoadOption);
	UPSLoadOption.yAxis[0].name = "%";
	UPSLoadOption.series[0].name = 'UPS Load Rate';
	UPSLoadOption.series[0].data = tempUpsload.default[0].yArray_data;
	UPSLoadOption.series[0].type='line';
	UPSLoadOption.xAxis[0].data = tempUpsload.Xdata[tempUpsload.default[1].datetype];
	UPSLoadchartName = echarts.init(document.getElementById('ups_load'));
	UPSLoadchartName.setOption(UPSLoadOption);

	$("#upsload_div > button").click(
		function(){
			reloadbase($(this).val(), tempUpsload, UPSLoadchartName);
	});
};


/*----- from serena -- start ---*/
function btn_toRight_onclick() {
	var objleft=document.getElementById("ctl00_ContentPlaceHolder1_ListBox3");
	var objright=document.getElementById("ctl00_ContentPlaceHolder1_ListBox2");  
	var objtest=document.getElementById("testright");
	var objtest2=document.getElementById("testleft");
	var i=0;
	while(i<objleft.options.length)
	{
		if(objleft.options[i].selected){
	    	  var n=objtest.options.length
	          objright.add(new Option(objleft.options[i].text,objleft.options[i].value));
	          objtest.add(new Option(objleft.options[i].text,objleft.options[i].value));
	          objleft.remove(i);
	          objtest2.remove(i);
	   	   	  objtest.options[n].selected=true;
	      }
	      else{
	          i++;
	      }
	} 
};
function btn_alltoRight_onclick() {
	var objleft=document.getElementById("ctl00_ContentPlaceHolder1_ListBox3");
	var objright=document.getElementById("ctl00_ContentPlaceHolder1_ListBox2");
	var objtest=document.getElementById("testright");
	var objtest2=document.getElementById("testleft");
	while(objleft.options.length!=0)
	{
		var n=objtest.options.length
		objright.add(new Option(objleft.options[0].text,objleft.options[0].value));
		objtest.add(new Option(objleft.options[0].text,objleft.options[0].value));
	        objleft.remove(0);
	        objtest2.remove(0);
	        objtest.options[n].selected=true;
	   }
	};
	function btn_toLeft_onclick() {
	  var objleft=document.getElementById("ctl00_ContentPlaceHolder1_ListBox3");
	  var objright=document.getElementById("ctl00_ContentPlaceHolder1_ListBox2"); 
	  var objtest=document.getElementById("testright");
	  var objtest2=document.getElementById("testleft");
	   var i=0;
	   while(i<objright.options.length)
	   {
	      if(objright.options[i].selected){
	    	  var n=objtest2.options.length
	          objleft.add(new Option(objright.options[i].text,objright.options[i].value));
	          objtest2.add(new Option(objright.options[i].text,objright.options[i].value));
	          objtest2.options[n].selected=true;
	          objright.remove(i);
	          objtest.remove(i);
	      }
	      else{
	          i++;
	      }
	   }  
	};
	function btn_alltoLeft_onclick() {
	  var objleft=document.getElementById("ctl00_ContentPlaceHolder1_ListBox3");
	  var objright=document.getElementById("ctl00_ContentPlaceHolder1_ListBox2");
	  var objtest=document.getElementById("testright"); 
	  var objtest2=document.getElementById("testleft");
	   while(objright.options.length!=0)
	   {
		    var n=objtest2.options.length
		    objleft.add(new Option(objright.options[0].text,objright.options[0].value));
	        objtest2.add(new Option(objright.options[0].text,objright.options[0].value));
	        objright.remove(0);
	        objtest.remove(0);
	        objtest2.options[n].selected=true;
	   }  
	};
	function exapand() {
		var obj=document.getElementById("selectorborder");
		var obj2=document.getElementById("showmore");
		var obj3=document.getElementById("angledown");
		if (obj.style.height=="50px") {
			obj.style.height="248px";
			obj2.childNodes[0].data = 'Hide ';
			obj3.className="fa fa-angle-double-up";
		}
		else {obj.style.height="50px";
			obj2.childNodes[0].data = 'Show more ';
			obj3.className="fa fa-angle-double-down";
		}
	};
	
	function exportGraphs(){
		if(navigator.userAgent.indexOf("MSIE")<0){
			alert("Please use IE browser!");
			return;
		}
		
		if (site_data != null){				
			try{     	            
	             var oXL = new ActiveXObject("Excel.Application");            
	             var oWB = oXL.Workbooks.Add();          
	             var oSheet = oWB.ActiveSheet;
	             var i, j;	 
	             
	             if(site_data.recordedEndtime)
	            	 oSheet.Cells(1, 1).Value = "Recorded End Time: " + site_data.recordedEndtime;
	             
	             if(site_data.fromdate && site_data.todate){
	            	 var period = site_data.fromdate + " - " + site_data.todate ;   
	            	 oSheet.Cells(2, 1).Value = period;
	             }
	             
	             if(site_data.obj_tc){
	             	var tempTC = eval(site_data.obj_tc);
	             	var length_x = tempTC.Xdata.day.length;
	             	var length_y = tempTC.Ydata.day.length;
	             	console.log("site_data1: " + tempTC.Xdata.day[0]);	
	             	if(length_x == length_y){           			
	             		oSheet.Cells(3, 1).Value = "Total Energy Consumption";             			
	             		oSheet.Cells(4, 1).value = "Date";
	             		oSheet.Cells(4, 2).value = "Value (kWh)";
	             		for (i = 0; i < length_x; i++){	             			       	          
	             			oSheet.Cells(i + 5, 1).value = tempTC.Xdata.day[i];
	             			oSheet.Cells(i + 5, 2).value = tempTC.Ydata.day[i];
	             		}
	             	}
	             }
	             
	             if(site_data.obj_adeff){
		             	var tempAdEff = eval(site_data.obj_adeff);
		             	var length_x = tempAdEff.Xdata.day.length;
		             	var length_y = tempAdEff.Ydata.day.length;
		             	console.log("site_data2: " + tempAdEff.Xdata.day[0]);	
		             	if(length_x == length_y){	             		
		             		oSheet.Cells(3, 4).Value = "Active Device Efficiency";	             			
		             		oSheet.Cells(4, 4).value = "Date";
		             		oSheet.Cells(4, 5).value = "Value (%)";
		             		for (i = 0; i < length_x; i++){	             			       	          
		             			oSheet.Cells(i + 5, 4).value = tempAdEff.Xdata.day[i];
		             			oSheet.Cells(i + 5, 5).value = tempAdEff.Ydata.day[i];
		             		}
		             	}
		             }
	             
	             if(site_data.reportviewdata.obj_pue){
		             	var tempPUE = eval(site_data.reportviewdata.obj_pue);
		             	var length_x = tempPUE.Xdata.day.length;
		             	var length_y = tempPUE.Ydata.day.length;
		             	console.log("site_data3: " + tempPUE.Xdata.day[0]);	
		             	if(length_x == length_y){	             		
		             		oSheet.Cells(3, 7).Value = "Power Usage Effectiveness";		           		
		             		oSheet.Cells(4, 7).value = "Date";
		             		oSheet.Cells(4, 8).value = "Value (-)";
		             		for (i = 0; i < length_x; i++){	             			       	          
		             			oSheet.Cells(i + 5, 7).value = tempPUE.Xdata.day[i];
		             			oSheet.Cells(i + 5, 8).value = tempPUE.Ydata.day[i];
		             		}
		             	}
		             }
	             
	             if(site_data.reportviewdata.obj_energy4pie){
		             	var tempEPie = eval(site_data.reportviewdata.obj_energy4pie);
		             	var length_x = tempEPie.length;
		             	var sum = 0;
		             	console.log("site_data4: " + tempEPie[0]);
		             	if(length_x==5){
		             		oSheet.Cells(3, 10).Value = "Energy Distribution";		           		
		             		oSheet.Cells(4, 10).value = "Category";
		             		oSheet.Cells(4, 11).value = "Value (KWh)";
		             		oSheet.Cells(4, 12).value = "Value (%)";
		             		
		             		oSheet.Cells(5, 10).Value = "Productive";
		             		oSheet.Cells(6, 10).Value = "Cooling";
		             		oSheet.Cells(7, 10).Value = "Active Device Loss";
		             		oSheet.Cells(8, 10).Value = "Lighting";
		             		oSheet.Cells(9, 10).Value = "Transmission";	 
		             		
		             		oSheet.Cells(5, 11).Value = tempEPie[0];
		             		oSheet.Cells(6, 11).Value = tempEPie[1];
		             		oSheet.Cells(7, 11).Value = tempEPie[2];
		             		oSheet.Cells(8, 11).Value = tempEPie[3];
		             		oSheet.Cells(9, 11).Value = tempEPie[4];	
		             		
		             		for (i = 0; i < length_x; i++){	             			       	          
		             			sum = sum + tempEPie[i];
		             		}
		             		
		             		for (i = 0; i < length_x; i++){	          
		             			var tmp = parseFloat(tempEPie[i]*100/sum);
		             			oSheet.Cells(i + 5, 12).value = tmp;
		             		}		             
		             	}	             		             			             		
		             }
	             
	             if(site_data.obj_dcload){
		             	var tempDcLoad = eval(site_data.obj_dcload);
		             	var length_x = tempDcLoad.Xdata.day.length;
		             	var length_y = tempDcLoad.Ydata.day.length;
		             	console.log("site_data5: " + tempDcLoad.Xdata.day[0]);	
		             	if(length_x == length_y){	             		
		             		oSheet.Cells(3, 14).Value = "DC Load Rate";		           		
		             		oSheet.Cells(4, 14).value = "Date";
		             		oSheet.Cells(4, 15).value = "Value (%)";
		             		for (i = 0; i < length_x; i++){	             			       	          
		             			oSheet.Cells(i + 5, 14).value = tempDcLoad.Xdata.day[i];
		             			oSheet.Cells(i + 5, 15).value = tempDcLoad.Ydata.day[i];
		             		}
		             	}
		             }
	             
	             if(site_data.obj_dceff){
		             	var tempDcEff = eval(site_data.obj_dceff);
		             	var length_x = tempDcEff.Xdata.day.length;
		             	var length_y = tempDcEff.Ydata.day.length;
		             	console.log("site_data6: " + tempDcEff.Xdata.day[0]);	
		             	if(length_x == length_y){	             		
		             		oSheet.Cells(3, 17).Value = "DC Efficiency";		           		
		             		oSheet.Cells(4, 17).value = "Date";
		             		oSheet.Cells(4, 18).value = "Value (%)";
		             		for (i = 0; i < length_x; i++){	             			       	          
		             			oSheet.Cells(i + 5, 17).value = tempDcEff.Xdata.day[i];
		             			oSheet.Cells(i + 5, 18).value = tempDcEff.Ydata.day[i];
		             		}
		             	}
		             }
	             
	             if(site_data.reportviewdata.obj_upsload){
		             	var tempUpsLoad = eval(site_data.reportviewdata.obj_upsload);
		             	var length_x = tempUpsLoad.Xdata.day.length;
		             	var length_y = tempUpsLoad.Ydata.day.length;
		             	console.log("site_data7: " + tempUpsLoad.Xdata.day[0]);	
		             	if(length_x == length_y){	             		
		             		oSheet.Cells(3, 20).Value = "UPS Load Rate";		           		
		             		oSheet.Cells(4, 20).value = "Date";
		             		oSheet.Cells(4, 21).value = "Value (%)";
		             		for (i = 0; i < length_x; i++){	             			       	          
		             			oSheet.Cells(i + 5, 20).value = tempUpsLoad.Xdata.day[i];
		             			oSheet.Cells(i + 5, 21).value = tempUpsLoad.Ydata.day[i];
		             		}
		             	}
		             }
	             
	             if(site_data.reportviewdata.obj_upseff){
		             	var tempUpsEff = eval(site_data.reportviewdata.obj_upseff);
		             	var length_x = tempUpsEff.Xdata.day.length;
		             	var length_y = tempUpsEff.Ydata.day.length;
		             	console.log("site_data8: " + tempUpsEff.Xdata.day[0]);	
		             	if(length_x == length_y){	             		
		             		oSheet.Cells(3, 23).Value = "UPS Efficiency";		           		
		             		oSheet.Cells(4, 23).value = "Date";
		             		oSheet.Cells(4, 24).value = "Value (%)";
		             		for (i = 0; i < length_x; i++){	             			       	          
		             			oSheet.Cells(i + 5, 23).value = tempUpsEff.Xdata.day[i];
		             			oSheet.Cells(i + 5, 24).value = tempUpsEff.Ydata.day[i];
		             		}
		             	}
		             } 
	             oXL.Visible = true; 	            
			}catch(e){
				alert("Can not open Excel applicaiton. Please confirm:\n1. Microsoft Excel has been installed. \n" +
						"2a. Lower the security level in Internet Options. \n" +
						"2b. Or reset: Internet Options -> Security -> Setting \"Enable unsafe ActiveX\"");  	            	                	            	       
			}         
		}
	};
	// Initialize the selector, realize the value re-filling and report display
	// after submit

	function select_data(data) {
		var reportlist = data.reportlist;
		var boxlist = data.boxlist;	
		var objtest=document.getElementById("testright");
		var objtest2=document.getElementById("testleft");
		var n=reportlist.length;
		var k=boxlist.length;
		for(var i=0;i<n;i++)
		   {
			  objtest.add(new Option(reportlist[i],reportlist[i]));
			  objtest.options[i].selected=true;
		   } 
		for(var i=0;i<k;i++)
		   {
			  objtest2.add(new Option(boxlist[i],boxlist[i]));
			  objtest2.options[i].selected=true;
		   }
		var objright=document.getElementById("ctl00_ContentPlaceHolder1_ListBox2"); 
		if(n>0)
		   {
			  for(var i=0;i<n;i++){
		      objright.add(new Option(objtest.options[i].text,objtest.options[i].value));}
		   }
		var objleft=document.getElementById("ctl00_ContentPlaceHolder1_ListBox3");
		if(k>0)
		   {
			  for(var i=0;i<k;i++){
		      objleft.add(new Option(objtest2.options[i].text,objtest2.options[i].value));}
		   }

	};
/*----- from serena -- end ---*/	

function HideAllCharts(){
	$("#dc_efficiency").hide();
	$("#ad_efficiency").hide();
	$("#dc_load_rate").hide();
	$("#total_consumption").hide();
	$("#alarms").hide();
	$("#ups_efficiency").hide();
	$("#upsload").hide();
	$("#pue").hide();
	$("#energy_distribution").hide();
};

function setDataAndShow(data){
	for (var i=0; i<data.reportfields.length;i++){
		switch(data.reportfields[i]){
		case 'DC Efficiency':
			$("#dc_efficiency").show();
			setDCEffChart(data.obj_dceff);
//			var textlist = ["%", "DC Efficiency"];
//			var DC_EffOption = '';
//			var DC_EffchartName = null;
//			setChart(DC_EffOption, data.obj_dceff, 'DCefficiency', '#dc_eff_div', textlist, DC_EffchartName);
			break;
		case 'Active Device Efficiency':
			$("#ad_efficiency").show();
			setADEffChart(data.obj_adeff);
//			var textlist = ["%", "AD Efficiency"];
//			var AD_EffOption = '';
//			var AD_EffchartName = null;
//			setChart(AD_EffOption, data.obj_adeff, 'ADefficiency', '#ad_eff_div', textlist, AD_EffchartName);
			break;
		case 'DC Load Rate':
			$("#dc_load_rate").show();
			setDCLoadChart(data.obj_dcload);
//			var textlist = ["%", "DC Load Rate"];
//			var DC_LoadOption = '';
//			var DC_LoadchartName = null;
//			setChart(DC_LoadOption, data.obj_dcload, 'DCloadrate', '#dc_load_div', textlist, DC_LoadchartName);
			break;
		case 'Total Energy Consumption':
			$("#total_consumption").show();
			setTCChart(data.obj_tc);
//			var textlist = ["kWh", "Total Consumption"];
//			var TCOption = '';
//			var TCchartName = null;
//			setChart(TCOption, data.obj_tc, 'TotalConsumption', '#tc_div', textlist, TCchartName);
			break;
		case 'Historical Event':
			$("#alarms").show();
			setAlarmTable(data.alarmData);
			break;
		case 'UPS Efficiency':
			$("#ups_efficiency").show();
			setUPSEffChart(data.reportviewdata.obj_upseff);
			break;
		case 'UPS Load Rate':
			$("#upsload").show();
			setUPSLoadChart(data.reportviewdata.obj_upsload);
			break;
		case 'Power Usage Effectiveness':
			$("#pue").show();
			setPUEChart(data.reportviewdata.obj_pue);
			break;
		case 'Energy Distribution':
			$("#energy_distribution").show();
			//setEnergyChart(data.reportviewdata.obj_energy);     //this is for 'stack bar' chart  of energy distribution
			setEnergyPieChart(data);               //this is for pie chart of energy distribution
			//alert(data.reportviewdata.obj_energy);
			break;
		default:
			break;
		};
	};
};
