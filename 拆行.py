'''
把大象装冰箱的三个步骤：
创建一个空白图像宽高1880*2660,白色(255,255,255)
将原图按顺序裁切成块
逐个将块横向粘贴到空白图像上并保存

'''

import os
from PIL import Image,ImageFilter


src = r"C:\Users\ygl\Desktop\ronghe"
dst =r"C:\Users\ygl\Desktop\横排"



def list2tuple(aList):      #两个一组
    return zip(aList[::2], aList[1::2])
    


def cropAndPaste(srcImgPath,dst):
    num = 1
    srcImgName = srcImgPath.split("\\")[-1]
    blankimg = Image.new("RGB",(1880,2660),(255,255,255))

    srcImg = Image.open(srcImgPath).convert("RGB")

    a,b,c,d = 2559,41,2628,1840     #竖行大框
    pasteA = 15
    pasteB = 15
    for i in range(0,16):#每半页16竖行
       
        Line = (a,b,c,d)
        a = a -75
        c = c -75
        rightHaltImg = srcImg.crop(Line).convert("RGB")
        contour = rightHaltImg.filter(ImageFilter.CONTOUR)
        imgW,imgH = contour.size
        img_arry = contour.load()
        
        cls = []
        for h in range(imgH):
            num = 0
            for w in range(imgW):
                if img_arry[w,h] ==(0,0,0):
                    num = num+1
            if num !=0:
                num =1
            else:
                num = 0
            cls.append(num)
        wordls = []
        length = len(cls)
       
        start = 0
        end = 0
        for n in range(0,length-1):
            if cls[n] ==0 and cls[n+1] ==1:
                wordls.append(n+1)
            if cls[n] ==1 and cls[n+1] ==0:
                wordls.append(n)

        listuple = list2tuple(wordls) 
        lotls = list(listuple)
        for m in range(0,len(lotls)):
            
            ab = 0
            bb = lotls[m][0]
            cb = imgW
            db = lotls[m][1]
            box = (ab,bb,cb,db)
            wordImg = rightHaltImg.crop(box)
            #wordImg.show()
            blankimg.paste(wordImg,box=(pasteA,pasteB))
            print(pasteA,pasteB)
            a = a-75
            c = c-75
            pasteA =pasteA +55
        pasteB = pasteB +60
            
    blankimg.save(dst+"\\"+srcImgName)

ls  = os.listdir(src)
for img in ls:
    imgpath = os.path.join(src,img)
    cropAndPaste(imgpath,dst)

