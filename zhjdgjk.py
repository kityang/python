from bs4 import BeautifulSoup as bs
import requests
import os


src = "/home/abc/Desktop/xinjian.txt"   #网页文件存储位置
txt = open("/home/abc/Desktop/test.txt",'w')  #最终结果存放位置
soup = bs(open(src,'r'),"html.parser")

volist = soup.ul.contents

for li0 in volist:
    juan = li0.p.a.get_text()
    txt.write(juan+"\n")
    ul1 = li0.ul
    if ul1 != None:
        li1 = ul1.contents
        for j in li1:
            pian = j.p.a.get_text()
            txt.write("    "+pian+"\n")
            ul2 = j.ul
            if ul2 != None:
                li2 = ul2.contents
                for k in li2:
                    zipian = k.p.a.get_text()
                    txt.write("        "+zipian+"\n")


txt.close()

