step = 2  #设定。步长不必逐行扫描，可隔行或隔多行，

def getEdgesHorizen(imgW,imgH,img_arry):# 水平图像，获得边界()，返回四个值
    top1 =top2 =top3 =top4 =0
    threshold = 120              #设定阈值为60个点
    center = 0
    H41 = int(imgH/4)
    H42 = int(imgH/2)
    H43 = int(imgH*3/4)


    
    for H in range(H41,0,-step):   #1/4处向上扫描，至顶部，统计水平线黑点个数
        blackPoint = 0
        for W in range(imgW):
            if img_arry[W,H] == 0:
                blackPoint = blackPoint+1
        if blackPoint <threshold:
            top1 = H
            break
        
    for H in range(H41,H42,step):    #1/4处向下扫描，至2/4处
        blackPoint = 0
        for W in range(imgW):
            if img_arry[W,H] == 0:
                blackPoint = blackPoint+1
       
        if blackPoint <threshold:
            top2 = H
            break
    for H in range(H43,H42,-step):     #3/4处向上扫描，至2/4处
        blackPoint = 0
        for W in range(imgW):
            if img_arry[W,H] == 0:
                blackPoint = blackPoint+1
        if blackPoint <threshold:
            top3 = H
            break

    for H in range(H43,imgH,step):   #3/4处向下扫描，至底部
        blackPoint = 0
        for W in range(imgW):
            if img_arry[W,H] == 0:
                blackPoint = blackPoint+1
        if blackPoint <threshold:
            top4 = H
            break

    return(top1,top2,top3,top4)


def getEdgesVertical(imgW,imgH,img_arry):   #垂直图像获取两个边界值，
    threshold = 120
    left = right = 0

    for W in range(int(imgW/4),0,-step):   #从1/4处向左扫描，统计垂直线黑点个数
        blackPoint = 0
        for H in range(imgH):
           
            if img_arry[W,H] == 0:
                blackPoint = blackPoint+1
            left = W
        if blackPoint <threshold:
            break
        

    for W in range(int(imgW/4*3),imgW,step): #从3/4处向右扫描，统计垂直线黑点个数
        blackPoint = 0
        for H in range(imgH):
            
            if img_arry[W,H] == 0:
                blackPoint = blackPoint+1
        if blackPoint <threshold:
            right = W
            break

    return(left,right)

