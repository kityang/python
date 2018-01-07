import os,re,csv,time,random
import requests
from urllib import request,parse
from bs4 import BeautifulSoup as bs
import traceback

head2={
'Accept':"",
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Cookie':"",
'Host':'',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.84'
}

host = r""
dst = r""
srcfi = csv.reader(open(r"fenlei.csv",'r'))

num = 1
for fenlei in srcfi:
    dir_name = fenlei[0]
    seed_url = fenlei[1]
    savedir = os.path.join(dst,dir_name)
    if not os.path.exists(savedir):
        os.mkdir(savedir)
   
    s_requ = requests.post(seed_url,headers=head2)  #post请求,获取每种分类的第一页，以此为基础，
    s_page = s_requ.text
    with open(os.path.join(savedir,"1.html"),'w')as html0:  #存储第一页
        html0.write(s_page)
        num = num+1
    s_soup = bs(s_page,"html.parser")   #将获取到的第一页转成html格式
    linkls = {}  
    als = s_soup.select(".next")[0].select("a") #将第一页底部的页码装入字典linkls{}
    for link in als:
        s_num = link.get_text()
        s_href = link.get("href")
        if s_num not in linkls:
            linkls[s_num] = s_href
    sumpage = s_soup.select("#ctl")[0].get_text()  #获得页面底部的 该小分类总页数
    st = sumpage[sumpage.find("/"):]
    page_num = int(re.findall("\d+",st)[0])  
    
    for i in range(2,page_num+1):    #循环下载，直到该小分类最后一页
        url = host + linkls[str(i)]
        savepath = savedir +"/"+str(i)+".html"
        num = num+1
        print(num,savepath)
        
        try:
            response = requests.post(url,headers=head2,timeout=5) 
            if response.status_code ==200:
                page = response.text
        except :
            #此处应将savepath写入日志，
            traceback.print_exc()

        #page = response.text
        
        
        
        if not os.path.exists(savepath):
            with open(savepath,'w')as html:
                html.write(page)
            
        newsoup = bs(page,"html.parser")
        newls = newsoup.select(".next")[0].select("a")
        linkls = {}
        for link in newls:
            pagenum = link.get_text()
            pagehref = link.get("href")
            if pagenum not in linkls:
                linkls[pagenum] = pagehref
        
        if num %100 ==0:
            time.sleep(5)  
        else:
            time.sleep(1+random.uniform(0,2))    


