var DateTimeShortcuts={calendars:[],calendarInputs:[],clockInputs:[],calendarDivName1:"calendarbox",calendarDivName2:"calendarin",calendarLinkName:"calendarlink",clockDivName:"clockbox",clockLinkName:"clocklink",admin_media_prefix:"",init:function(){var b=document.getElementsByTagName("script");for(var d=0;d<b.length;d++){if(b[d].src.match(/DateTimeShortcuts/)){var a=b[d].src.indexOf("js/admin/DateTimeShortcuts");DateTimeShortcuts.admin_media_prefix=b[d].src.substring(0,a);break}}var c=document.getElementsByTagName("input");for(d=0;d<c.length;d++){var e=c[d];if(e.getAttribute("type")=="text"&&e.className.match(/vTimeField/)){DateTimeShortcuts.addClock(e)}else{if(e.getAttribute("type")=="text"&&e.className.match(/vDateField/)){DateTimeShortcuts.addCalendar(e)}}}},addClock:function(e){var c=DateTimeShortcuts.clockInputs.length;DateTimeShortcuts.clockInputs[c]=e;var a=document.createElement("span");e.parentNode.insertBefore(a,e.nextSibling);var d=document.createElement("a");d.setAttribute("href","javascript:DateTimeShortcuts.handleClockQuicklink("+c+", new Date().getHourMinuteSecond());");d.appendChild(document.createTextNode(gettext("Now")));var b=document.createElement("a");b.setAttribute("href","javascript:DateTimeShortcuts.openClock("+c+");");b.id=DateTimeShortcuts.clockLinkName+c;quickElement("img",b,"","src",DateTimeShortcuts.admin_media_prefix+"img/admin/icon_clock.gif","alt",gettext("Clock"));a.appendChild(document.createTextNode("\240"));a.appendChild(d);a.appendChild(document.createTextNode("\240|\240"));a.appendChild(b);var f=document.createElement("div");f.style.display="none";f.style.position="absolute";f.className="clockbox module";f.setAttribute("id",DateTimeShortcuts.clockDivName+c);document.body.appendChild(f);addEvent(f,"click",DateTimeShortcuts.cancelEventPropagation);quickElement("h2",f,gettext("Choose a time"));time_list=quickElement("ul",f,"");time_list.className="timelist";quickElement("a",quickElement("li",time_list,""),gettext("Now"),"href","javascript:DateTimeShortcuts.handleClockQuicklink("+c+", new Date().getHourMinuteSecond());");quickElement("a",quickElement("li",time_list,""),gettext("Midnight"),"href","javascript:DateTimeShortcuts.handleClockQuicklink("+c+", '00:00:00');");quickElement("a",quickElement("li",time_list,""),gettext("6 a.m."),"href","javascript:DateTimeShortcuts.handleClockQuicklink("+c+", '06:00:00');");quickElement("a",quickElement("li",time_list,""),gettext("Noon"),"href","javascript:DateTimeShortcuts.handleClockQuicklink("+c+", '12:00:00');");cancel_p=quickElement("p",f,"");cancel_p.className="calendar-cancel";quickElement("a",cancel_p,gettext("Cancel"),"href","javascript:DateTimeShortcuts.dismissClock("+c+");")},openClock:function(b){var c=document.getElementById(DateTimeShortcuts.clockDivName+b);var a=document.getElementById(DateTimeShortcuts.clockLinkName+b);if(getStyle(document.body,"direction")!="rtl"){c.style.left=findPosX(a)+17+"px"}else{c.style.left=findPosX(a)-110+"px"}c.style.top=findPosY(a)-30+"px";c.style.display="block";addEvent(window.document,"click",function(){DateTimeShortcuts.dismissClock(b);return true})},dismissClock:function(a){document.getElementById(DateTimeShortcuts.clockDivName+a).style.display="none";window.document.onclick=null},handleClockQuicklink:function(a,b){DateTimeShortcuts.clockInputs[a].value=b;DateTimeShortcuts.dismissClock(a)},addCalendar:function(g){var d=DateTimeShortcuts.calendars.length;DateTimeShortcuts.calendarInputs[d]=g;var f=document.createElement("span");g.parentNode.insertBefore(f,g.nextSibling);var j=document.createElement("a");j.setAttribute("href","javascript:DateTimeShortcuts.handleCalendarQuickLink("+d+", 0);");j.appendChild(document.createTextNode(gettext("Today")));var b=document.createElement("a");b.setAttribute("href","javascript:DateTimeShortcuts.openCalendar("+d+");");b.id=DateTimeShortcuts.calendarLinkName+d;quickElement("img",b,"","src",DateTimeShortcuts.admin_media_prefix+"img/admin/icon_calendar.gif","alt",gettext("Calendar"));f.appendChild(document.createTextNode("\240"));f.appendChild(j);f.appendChild(document.createTextNode("\240|\240"));f.appendChild(b);var i=document.createElement("div");i.style.display="none";i.style.position="absolute";i.className="calendarbox module";i.setAttribute("id",DateTimeShortcuts.calendarDivName1+d);document.body.appendChild(i);addEvent(i,"click",DateTimeShortcuts.cancelEventPropagation);var c=quickElement("div",i,"");var h=quickElement("a",c,"<","href","javascript:DateTimeShortcuts.drawPrev("+d+");");h.className="calendarnav-previous";var k=quickElement("a",c,">","href","javascript:DateTimeShortcuts.drawNext("+d+");");k.className="calendarnav-next";var l=quickElement("div",i,"","id",DateTimeShortcuts.calendarDivName2+d);l.className="calendar";DateTimeShortcuts.calendars[d]=new Calendar(DateTimeShortcuts.calendarDivName2+d,DateTimeShortcuts.handleCalendarCallback(d));DateTimeShortcuts.calendars[d].drawCurrent();var e=quickElement("div",i,"");e.className="calendar-shortcuts";quickElement("a",e,gettext("Yesterday"),"href","javascript:DateTimeShortcuts.handleCalendarQuickLink("+d+", -1);");e.appendChild(document.createTextNode("\240|\240"));quickElement("a",e,gettext("Today"),"href","javascript:DateTimeShortcuts.handleCalendarQuickLink("+d+", 0);");e.appendChild(document.createTextNode("\240|\240"));quickElement("a",e,gettext("Tomorrow"),"href","javascript:DateTimeShortcuts.handleCalendarQuickLink("+d+", +1);");var a=quickElement("p",i,"");a.className="calendar-cancel";quickElement("a",a,gettext("Cancel"),"href","javascript:DateTimeShortcuts.dismissCalendar("+d+");")},openCalendar:function(b){var c=document.getElementById(DateTimeShortcuts.calendarDivName1+b);var a=document.getElementById(DateTimeShortcuts.calendarLinkName+b);var e=DateTimeShortcuts.calendarInputs[b];if(e.value){var f=e.value.split("-");var d=f[0];var g=parseFloat(f[1]);if(d.match(/\d\d\d\d/)&&g>=1&&g<=12){DateTimeShortcuts.calendars[b].drawDate(g,d)}}if(getStyle(document.body,"direction")!="rtl"){c.style.left=findPosX(a)+17+"px"}else{c.style.left=findPosX(a)-180+"px"}c.style.top=findPosY(a)-75+"px";c.style.display="block";addEvent(window.document,"click",function(){DateTimeShortcuts.dismissCalendar(b);return true})},dismissCalendar:function(a){document.getElementById(DateTimeShortcuts.calendarDivName1+a).style.display="none";window.document.onclick=null},drawPrev:function(a){DateTimeShortcuts.calendars[a].drawPreviousMonth()},drawNext:function(a){DateTimeShortcuts.calendars[a].drawNextMonth()},handleCalendarCallback:function(a){return"function(y, m, d) { DateTimeShortcuts.calendarInputs["+a+"].value = y+'-'+(m<10?'0':'')+m+'-'+(d<10?'0':'')+d; document.getElementById(DateTimeShortcuts.calendarDivName1+"+a+").style.display='none';}"},handleCalendarQuickLink:function(a,c){var b=new Date();b.setDate(b.getDate()+c);DateTimeShortcuts.calendarInputs[a].value=b.getISODate();DateTimeShortcuts.dismissCalendar(a)},cancelEventPropagation:function(a){if(!a){a=window.event}a.cancelBubble=true;if(a.stopPropagation){a.stopPropagation()}}};addEvent(window,"load",DateTimeShortcuts.init);