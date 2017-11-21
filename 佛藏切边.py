import os
from PIL import Image,ImageFilter


def getBox(top,down,left,right,imgW,imgH,img_arry):
    for topP in range(0,int(imgH/2)):
        num = 0
        for w in range(imgW):
            if img_arry[w,topP] ==(0,0,0):
                num = num +1
        if num >(imgW*0.6):
            top = topP
            break


    for downN in range(imgH,int(imgH/2),-1):
        num = 0
        for w in range(imgW):
            if img_arry[w,downN-1] ==(0,0,0):
                num = num +1
        if num >(imgW*0.6):
            down = downN
            break

    for leftT in range(0,int(imgW/2)):
        num = 0
        for h in range(imgH):
            if img_arry[leftT,h] ==(0,0,0):
                num = num +1
        if num >(imgH*0.6):
            left = leftT
            break


    for rightT in range(imgW,int(imgW/2),-1):
        num = 0
        for h in range(imgH):
            if img_arry[rightT-1,h] ==(0,0,0):
                num = num +1
        if num >(imgH*0.5):
            right = rightT
            break
    box = (left,top,right,down)
    return box

    

src  = r"C:\Users\ygl\Desktop\png\png"
dst = r"C:\Users\ygl\Desktop\png\切边后文件"

ls = os.listdir(src)

for i in ls:
    srcimgpath = os.path.join(src,i)
    dstimgpath = os.path.join(dst,i)
    

    img = Image.open(srcimgpath).convert("RGB")
    img_arry = img.load()
    imgW,imgH = img.size

    top = 0
    down = 0
    left = 0
    right = 0

    box = getBox(top,down,left,right,imgW,imgH,img_arry)
    newImg = img.crop(box)
    newImg.save(dstimgpath)
      

