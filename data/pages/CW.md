- #место
- Тип:: Магазин
- Локация:: [[Австралия]]
- [[2025-04-28 ClearCreditCardDetails]]
- [[2025-05-03 May Statistics Graph]]
- [[2025-05-05 URL]]
- [[2025-05-06 CatTrail]]
- [[2025-05-10 Research]]
- [[2025-05-13 Email]]
- [[2025-05-15 Email save Sent]]
- [[2025-05-20 nofollow wishlist.php]]
- 2025-05-24 [[P - CW 301]]
	- DONE 301 для CIGARS
	- TODO 301 для страниц без слэш в конец
- [[2025-06-02 Update Prices]]
- [[2025-06-03 Health Banners]]
- [[2025-06-05 301 for canonical]]
-
- Todo
	- 301
		- , to %2C
		- & to %26
	- add canonical - pages.php
	- Page indexing - Not found (404)
	- add news - on Mobile
	- Fix Feedback Forms
		- Contact Us - From address
		- FAQ's
	- Туду [[CW]] fix All Time Graph
		- https://www.cigarworld.com.au/aud/admin/index.php?ToDo=viewStats
		- https://www.cigarworld.com.au/aud/admin/index.php?ToDo=overviewStatsData&from=1343261433&to=1749053997
-
- Orders from Mobile and PC on Google Analytics
	- Home -> Key Events by Platform
-
- Visual Stability is poor but improving
	- https://cruxvis.withgoogle.com/#/?view=cwvsummary&url=https%3A%2F%2Fwww.cigarworld.com.au%2Faud%2F&identifier=url&device=PHONE&periodStart=0&periodEnd=-1&display=p75s
-
- Cache Check
	- https://www.giftofspeed.com/cache-checker/
	-
- Analytics module
	- gtag.js is required by google analytics
	-
- SMTP Relay Test из PHP
	- https://chatgpt.com/c/680b875a-4990-800d-98ea-a2b42d372a30
	-
- Original Files v.6.1.1
	- 1 https://github.com/rockdrigo/Inte_lisis_Store_ecommerce/tree/master/branch/devel-3.0-acuario
	- 2 https://github.com/szwork2013/modify/
	-
- основные изменения
	- mysql.php: require adapter, use is_db_resource()
	- db.php: use is_db_resource()
	- ? admin/init.php: comment UPGRADE
	- config.php: EnableSEOUrls = 0
	- lib/general.php: // sitex 15/10/2017 - redirect fake domains
	- .gitattribute: * -text
		- git add --renormalize .
		- git reset --hard
- 2025-05-01 Connect Search Console to Google Analytics
- 2025-05-01 новый код отслеживания от GA
	- было
		- ```
		      <script>
		          if (navigator.userAgent.indexOf("Speed Insights") == -1) {
		          (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
		                  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
		              m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
		          })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
		          ga('create', 'UA-92882006-1', 'auto');
		          ga('send', 'pageview');
		          }
		      </script>
		  ```
	- стало
		- ```
		  <script async="" src="https://www.googletagmanager.com/gtag/js?id=G-E89EBMRENT"></script>
		  <script>
		    window.dataLayer = window.dataLayer || [];
		    function gtag(){dataLayer.push(arguments);}
		    gtag('js', new Date());
		    gtag('config', 'G-E89EBMRENT');
		  </script>
		  ```
	- стало 2
		- ```
		  <script>
		  enScroll=!1,enFdl=!1,extCurrent=void 0,filename=void 0,targetText=void 0,splitOrigin=void 0;const lStor=localStorage,sStor=sessionStorage,doc=document,docEl=document.documentElement,docBody=document.body,docLoc=document.location,w=window,s=screen,nav=navigator||{},extensions=["pdf","xls","xlsx","doc","docx","txt","rtf","csv","exe","key","pps","ppt","pptx","7z","pkg","rar","gz","zip","avi","mov","mp4","mpe","mpeg","wmv","mid","midi","mp3","wav","wma"];function a(e,t,n,o){const j="G-E89EBMRENT",r=()=>Math.floor(Math.random()*1e9)+1,c=()=>Math.floor(Date.now()/1e3),F=()=>(sStor._p||(sStor._p=r()),sStor._p),E=()=>r()+"."+c(),_=()=>(lStor.cid_v4||(lStor.cid_v4=E()),lStor.cid_v4),m=lStor.getItem("cid_v4"),v=()=>m?void 0:enScroll==!0?void 0:"1",p=()=>(sStor.sid||(sStor.sid=c()),sStor.sid),O=()=>{if(!sStor._ss)return sStor._ss="1",sStor._ss;if(sStor.getItem("_ss")=="1")return void 0},a="1",g=()=>{if(sStor.sct)if(enScroll==!0)return sStor.sct;else x=+sStor.getItem("sct")+ +a,sStor.sct=x;else sStor.sct=a;return sStor.sct},i=docLoc.search,b=new URLSearchParams(i),h=["q","s","search","query","keyword"],y=h.some(e=>i.includes("&"+e+"=")||i.includes("?"+e+"=")),u=()=>y==!0?"view_search_results":enScroll==!0?"scroll":enFdl==!0?"file_download":"page_view",f=()=>enScroll==!0?"90":void 0,C=()=>{if(u()=="view_search_results"){for(let e of b)if(h.includes(e[0]))return e[1]}else return void 0},d=encodeURIComponent,k=e=>{let t=[];for(let n in e)e.hasOwnProperty(n)&&e[n]!==void 0&&t.push(d(n)+"="+d(e[n]));return t.join("&")},A=!1,S="https://www.google-analytics.com/g/collect",M=k({v:"2",tid:j,_p:F(),sr:(s.width*w.devicePixelRatio+"x"+s.height*w.devicePixelRatio).toString(),ul:(nav.language||void 0).toLowerCase(),cid:_(),_fv:v(),_s:"1",dl:docLoc.origin+docLoc.pathname+i,dt:doc.title||void 0,dr:doc.referrer||void 0,sid:p(),sct:g(),seg:"1",en:u(),"epn.percent_scrolled":f(),"ep.search_term":C(),"ep.file_extension":e||void 0,"ep.file_name":t||void 0,"ep.link_text":n||void 0,"ep.link_url":o||void 0,_ss:O(),_dbg:A?1:void 0}),l=S+"?"+M;if(nav.sendBeacon)nav.sendBeacon(l);else{let e=new XMLHttpRequest;e.open("POST",l,!0)}}a();function sPr(){return(docEl.scrollTop||docBody.scrollTop)/((docEl.scrollHeight||docBody.scrollHeight)-docEl.clientHeight)*100}doc.addEventListener("scroll",sEv,{passive:!0});function sEv(){const e=sPr();if(e<90)return;enScroll=!0,a(),doc.removeEventListener("scroll",sEv,{passive:!0}),enScroll=!1}document.addEventListener("DOMContentLoaded",function(){let e=document.getElementsByTagName("a");for(let t=0;t<e.length;t++)if(e[t].getAttribute("href")!=null){const n=e[t].getAttribute("href"),s=n.substring(n.lastIndexOf("/")+1),o=s.split(".").pop();(e[t].hasAttribute("download")||extensions.includes(o))&&e[t].addEventListener("click",fDl,{passive:!0})}});function fDl(e){enFdl=!0;const t=e.currentTarget.getAttribute("href"),n=t.substring(t.lastIndexOf("/")+1),s=n.split(".").pop(),o=n.replace("."+s,""),i=e.currentTarget.text,r=t.replace(docLoc.origin,"");a(s,o,i,r),enFdl=!1}
		  </script>
		  ```