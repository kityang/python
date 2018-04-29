#!/usr/bin/python3
'''
网上好多扫描PDF被加上了广告，这个广告商都倒闭多年了
ubuntu下没有好用的删除pdf页面的工具
pdf2single()将pdf拆成单页
pdfmerge()将pdf合并成一个。linux下文件乱序，需要sort()一下。
'''

import os,io
from PyPDF2 import PdfFileReader,PdfFileWriter,PdfFileMerger

def pdf2single(pdf,dst):
    pdfbook = PdfFileReader(open(pdf,'rb'))
    pnum =pdfbook.getNumPages()
    for i in range(1,pnum):
        pdfw =PdfFileWriter()
        page =pdfbook.getPage(i)
        pname = os.path.join(dstpath,"{:0>4d}".format(i)+".pdf")
        pdfw.addPage(page)
        pdfw.write(open(pname,'wb'))
   
def pdfmerge(pdfpagesdir,dstpath):
    pdfbook = PdfFileWriter()
    ls = os.listdir(pdfpagesdir)
    ls.sort()
    for i in ls:
        page = PdfFileReader(open(os.path.join(pdfpagesdir,i),'rb'))
        pdfbook.appendPagesFromReader(page)
    pdfbook.write(open(dstpath,'wb'))

src ='/home/abc/Desktop/pdf'
dst ='/home/abc/Desktop/singlepdf'

'''
for f in os.listdir(src):
    name = f.split(".")[0]
    dstpath = os.path.join(dst,name)
    if not os.path.exists(dstpath):
        os.mkdir(dstpath)
    pdf = os.path.join(src,f)    
    pdf2single(pdf,dstpath) 
    print(dstpath)
'''
pdfdir = '/home/abc/Desktop/singlepdf/深入分析JavaWeb技术内幕'
savep = '/home/abc/Desktop/singlepdf/深入分析JavaWeb技术内幕.pdf'
pdfmerge(pdfdir,savep)

print("结束")
        
