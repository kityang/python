
import os,gc
from PIL import Image,ImageFilter
import my_imge        #自定义模块，在此脚本同文件夹下


def img_cut(src,dst,i):
    srcimgpath = os.path.join(src,i)
    dstimgpath = os.path.join(dst,i)
    name = i.split(".")[0]
    
    img = Image.open(srcimgpath).convert("1")

    img_arry = img.load()
    imgW,imgH = img.size

    edge = my_imge.getEdgesByTH(imgW,imgH,img_arry)
    
    box = (edge[0],edge[2],edge[1],edge[3])

    srcimg = Image.open(srcimgpath).convert("1")
    img = srcimg.crop(box)
    img.save(os.path.join(dst,name+".png"))
    




source  = r"C:\Users\cbs-shenzhou-001\Desktop\永乐北藏拆图\永乐北藏原始"
dest = r"C:\Users\cbs-shenzhou-001\Desktop\永乐北藏拆图\永乐北藏切图"
txt_all = open(r"C:\Users\cbs-shenzhou-001\Desktop\永乐北藏拆图\log1.txt",'w')
txt_blank = open(r"C:\Users\cbs-shenzhou-001\Desktop\永乐北藏拆图\空白页.txt",'w')

for dirs in os.listdir(source):
    srcdirpath = os.path.join(source,dirs)
    dstdirpath = os.path.join(dest,dirs)
    if not os.path.exists(dstdirpath):
        os.makedirs(dstdirpath)

    for img in os.listdir(srcdirpath):
        imgpath = os.path.join(srcdirpath,img)
        txt_all.write("%s\n"%(imgpath))
        print (img)
        img_cut(srcdirpath,dstdirpath,img)
        gc.collect()

    print (srcdirpath)

    
txt_all.close()
txt_blank.close()

    
    
      

