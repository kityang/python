#coding:cp936
'''
ê��1/4,�������º���ɨ�裬һ��ÿ�еĺڵ�����������ֵ�����Ϊ�߽磬ֹͣ
ê��3/4,�������º���ɨ�裬һ��ÿ�еĺڵ�����������ֵ�����Ϊ�߽磬ֹͣ
תΪ�Ҷ�ͼ���趨��ֵΪ100��תΪ��ֵ
'''
import os,gc
from PIL import Image,ImageFilter
import my_imge                   #�Զ���ģ�飬�ڴ˽ű�ͬ�ļ�����



def img_cut(src,dst,i):
    srcimgpath = os.path.join(src,i)
    dstimgpath = os.path.join(dst,i)
    name = i.split(".")[0]
    
    img = Image.open(srcimgpath).convert("1")

    img_arry = img.load()
    imgW,imgH = img.size


    threshold = 120              
    center = 0
    
    for H in range(int(imgH/2),int(imgH/2)+1):
        blackPoint = 0
        for W in range(imgW):
            if img_arry[W,H] == 0:
                blackPoint = blackPoint+1
                
        center = blackPoint
    
    
    if center<=120:
        tops = my_imge.getEdgesHorizen(imgW,imgH,img_arry)
        box1 = (0,tops[0],imgW,tops[1])
        box2 = (0,tops[2],imgW,tops[3])

        H1 = (tops[1]-tops[0])
        H2 = (tops[3]-tops[2])

        srcimg = Image.open(srcimgpath).convert("L")
        img1 = srcimg.crop(box1).resize((int(imgW/2),int(H1/2)))
        img2 = srcimg.crop(box2).resize((int(imgW/2),int(H2/2)))
        
        threshold2 = 100
        table = []
        for j in range(256):
            if j < threshold2:
                table.append(0)
            else:
                table.append(1)

        imgpng1 = img1.point(table, '1')
        imgpng2 = img2.point(table, '1')

        imgpng1.save(os.path.join(dst,name+"_1.png"))
        imgpng2.save(os.path.join(dst,name+"_2.png"))
        print(center+"ˮƽ",dst,i)
    else:
        leftright = my_imge.getEdgesVertical(imgW,imgH,img_arry)
        
        box = (leftright[0],0,leftright[1],imgH)
        
        w2 = leftright[1]-leftright[0]
        srcimg = Image.open(srcimgpath).convert("L")
        img1 = srcimg.crop(box).resize((int(w2/2),int(imgH/2)))
        threshold2 = 100
        table = []
        for j in range(256):
            if j < threshold2:
                table.append(0)
            else:
                table.append(1)

        imgpng1 = img1.point(table, '1')
        imgpng1.save(os.path.join(dst,name+"_1.png"))
        print (center+"��ֱ",dst,i)




source  = r"/media/abc/һ��¿/dunhuangsrc/"
dest = r"/media/abc/һ��¿/dunhuangresult"
txt = open(r"/media/abc/һ��¿/dunhuangresult/�ػ���ͼlog1.txt",'w')

for dirs in os.listdir(source):
    srcdirpath = os.path.join(source,dirs)
    dstdirpath = os.path.join(dest,dirs)

    for img in os.listdir(srcdirpath):
        imgpath = os.path.join(srcdirpath,img)
        txt.write("%s\n"%(imgpath))
        img_cut(srcdirpath,dstdirpath,img)
        gc.collect()


    
    
    
    
      

