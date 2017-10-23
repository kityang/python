'''
把大象装冰箱的三个步骤：
创建一个空白图像宽高1880*2660,白色(255,255,255)
将原图按顺序裁切成块
逐个将块横向粘贴到空白图像上并保存

'''

import os
from PIL import Image,ImageFilter


src = r"C:\Users\ygl\Desktop\ps切边"
dst =r"C:\Users\ygl\Desktop\横排"
new = r"C:\Users\ygl\Desktop\新建文件夹"


def cropAndPaste(srcImgPath,dst):
    num = 1
    srcImgName = srcImgPath.split("\\")[-1]
    blankimg = Image.new("RGB",(1880,2660),(255,255,255))

    srcImg = Image.open(srcImgPath).convert("RGB")
    pasteA = 15
    pasteB = 15
    a,b,c,d = 2559,41,2628,1840     #竖行大框
    e,g= 2565,2620     #单字小框
    for i in range(0,16):           #每半页16竖行
        Line = (a,b,c,d)
        a = a -75
        c = c -75
        rightHaltImg = srcImg.crop(Line).convert("RGB")
        
        f,h = 58,118
        for j in range(0,30):       #每竖行30字
            Word = (e,f,g,h)
            
            wordImg = srcImg.crop(Word)
            #wordImg.show()
            num = num+1
            f = f +58
            h = h +58
            blankimg.paste(wordImg,box=(pasteA,pasteB))
            pasteA =pasteA +55
        e = e -75
        g = g -75
        pasteA = 16
        pasteB = pasteB +60
            
    blankimg.save(dst+"\\"+srcImgName)

ls  = os.listdir(src)
for img in ls:
    imgpath = os.path.join(src,img)
    cropAndPaste(imgpath,dst)

