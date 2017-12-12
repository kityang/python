

step = 2  #设定。步长不必逐行扫描，可隔行或隔多行，


def isBlank(imgW,imgH,img_arry):      #判断图片是否是空白图像
    horizon = 0
    verticle = 0
    for H in range(int(imgH/2),int(imgH/2)+1):
        blackPoint = 0
        for W in range(imgW):
            if img_arry[W,H] == 0:
                blackPoint = blackPoint+1
        horizon = blackPoint
        
    for W in range(int(imgW/2),int(imgW/2)+1):
        blackPoint = 0
        for H in range(imgH):
            if img_arry[W,H] == 0:
                blackPoint = blackPoint+1
        verticle = blackPoint

    if horizon <=20 or  verticle <=20:
        return True
    else:
        return False

def getEdges(imgW,imgH,img_arry): #获取四个边界,设定四个阈值
    left = right = top = down =0
    thresholdLeft = 450
    thresholdRight = 450
    thresholdTop = int(imgW*0.5)
    thresholdDown = int(imgW*0.5)
    
    

    for W in range(30,int(imgW/2),step): #从左向中间
        blackPoint = 0
        for H in range(imgH):
            if img_arry[W,H] == 0:
                blackPoint = blackPoint+1
        if blackPoint > thresholdLeft:
            left = W
            break
    for W in range(imgW-100,int(imgW/4*3),-step): #从右向中间
        blackPoint = 0
        for H in range(imgH):
            if img_arry[W,H] == 0:
                blackPoint = blackPoint+1
        if blackPoint > thresholdRight:
            right = W
            break

    for H in range(30,int(imgH/4),step):   #从上往下
        blackPoint = 0
        for W in range(imgW):
            if img_arry[W,H] ==0:
                blackPoint = blackPoint + 1
        if blackPoint > thresholdTop:
            top = H
            break

    for H in range(imgH-100,int(imgH/4*3),-step):   #从下往
        blackPoint = 0
        for W in range(imgW):
            if img_arry[W,H] ==0:
                blackPoint = blackPoint + 1
        if blackPoint > thresholdDown:
            down = H
            break

    return (left,right,top,down)
 
        
def getEdgesByTH(imgW,imgH,img_arry):

    left_cut = 0
    right_cut = 10
    top_cut = 0
    down_cut = 10
    
    bktopls =[]
    for W in range(0,int(imgW/4)):
        bk = 0
        for H in range(imgH):
            if img_arry[W,H]==0:
                bk = bk+1
        bktopls.append(bk)
    for i in range(100,len(bktopls)):
        avg = 0
        if bktopls[i] >10:
            a1 = bktopls[i]
            a2 = bktopls[i+1]
            a3 = bktopls[i+2]
            a4 = bktopls[i+3]
            a5 = bktopls[i+4]
            avg =((a1+a2+a3+a4+a5)/5)
            if 10<avg:
                if avg<100:
                    left_cut = i+70
                else:
                    left_cut = i+30
                break


    bktoplsR =[]
    for W in range(imgW-100,int(imgW/2+10),-1):
        bk = 0
        for H in range(imgH):
            if img_arry[W,H]==0:
                bk = bk+1

        bktoplsR.append((bk,W))
    
    for i in range(0,len(bktoplsR)):
        avg = 0
        if bktoplsR[i][0] >10:
            a1 = bktoplsR[i][0]
            a2 = bktoplsR[i+1][0]
            a3 = bktoplsR[i+2][0]
            a4 = bktoplsR[i+3][0]
            a5 = bktoplsR[i+4][0]
            avg =((a1+a2+a3+a4+a5)/5)
            if 10<avg:
                if avg<100:
                    right_cut = bktoplsR[i][1]-70
                else:
                    right_cut = bktoplsR[i][1]-30
                break
       
                  
    for H in range(30,int(imgH/4)):
        bk = 0
        for W in range(imgW):
            if img_arry[W,H]==0:
                bk = bk+1
        if bk >100:
            top_cut = H+40
            break
    for H in range(imgH-5,int(imgH/4*3),-1):
        bk = 0
        for W in range(imgW):
            if img_arry[W,H]==0:
                bk = bk+1
        if bk >100:
            down_cut = H-35
            break

    return(left_cut,right_cut,top_cut,down_cut)





















    
