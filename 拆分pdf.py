import os,io
from PyPDF2 import PdfFileReader,PdfFileWriter,PdfFileMerger

src =r"H:\PDF"
dst =r"C:\Users\pdf"

lis = os.listdir(src)


for f in lis:
    name = f.split(".")[0]
    dstpath = os.path.join(dst,name)
    if not os.path.exists(dstpath):
        os.mkdir(dstpath)
    pdfbook = PdfFileReader(open(os.path.join(src,f),'rb'))
    pnum =pdfbook.getNumPages()
    for i in range(1,pnum):
        pdfw =PdfFileWriter()
        page =pdfbook.getPage(i)
        pname = os.path.join(dstpath,"{:0>4d}".format(i)+".pdf")
        pdfw.addPage(page)
        pdfw.write(open(pname,'wb'))
        

    print(dstpath)

print("结束")
        
