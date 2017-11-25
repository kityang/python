step = 2  #�趨��������������ɨ�裬�ɸ��л�����У�

def getEdgesHorizen(imgW,imgH,img_arry):# ˮƽͼ�񣬻�ñ߽�()�������ĸ�ֵ
    top1 =top2 =top3 =top4 =0
    threshold = 120              #�趨��ֵΪ60����
    center = 0
    H41 = int(imgH/4)
    H42 = int(imgH/2)
    H43 = int(imgH*3/4)


    
    for H in range(H41,0,-step):   #1/4������ɨ�裬��������ͳ��ˮƽ�ߺڵ����
        blackPoint = 0
        for W in range(imgW):
            if img_arry[W,H] == 0:
                blackPoint = blackPoint+1
        if blackPoint <threshold:
            top1 = H
            break
        
    for H in range(H41,H42,step):    #1/4������ɨ�裬��2/4��
        blackPoint = 0
        for W in range(imgW):
            if img_arry[W,H] == 0:
                blackPoint = blackPoint+1
       
        if blackPoint <threshold:
            top2 = H
            break
    for H in range(H43,H42,-step):     #3/4������ɨ�裬��2/4��
        blackPoint = 0
        for W in range(imgW):
            if img_arry[W,H] == 0:
                blackPoint = blackPoint+1
        if blackPoint <threshold:
            top3 = H
            break

    for H in range(H43,imgH,step):   #3/4������ɨ�裬���ײ�
        blackPoint = 0
        for W in range(imgW):
            if img_arry[W,H] == 0:
                blackPoint = blackPoint+1
        if blackPoint <threshold:
            top4 = H
            break

    return(top1,top2,top3,top4)


def getEdgesVertical(imgW,imgH,img_arry):   #��ֱͼ���ȡ�����߽�ֵ��
    threshold = 120
    left = right = 0

    for W in range(int(imgW/4),0,-step):   #��1/4������ɨ�裬ͳ�ƴ�ֱ�ߺڵ����
        blackPoint = 0
        for H in range(imgH):
           
            if img_arry[W,H] == 0:
                blackPoint = blackPoint+1
            left = W
        if blackPoint <threshold:
            break
        

    for W in range(int(imgW/4*3),imgW,step): #��3/4������ɨ�裬ͳ�ƴ�ֱ�ߺڵ����
        blackPoint = 0
        for H in range(imgH):
            
            if img_arry[W,H] == 0:
                blackPoint = blackPoint+1
        if blackPoint <threshold:
            right = W
            break

    return(left,right)

