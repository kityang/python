'''
百度文字识别2017-11份尚无文字方向参数，竖排页面的识别结果需要重新排序
使用位置信息版OCR，根据识别块的重心进行排序，先左后右，先上后下，

'''


import os,json

def widthAverage(words_result):
    w = 0
    for i in words_result:
    
        location = i["location"]
        width = location['width']
        w = w +width

    return int(w/(len(words_result)))
        
def sortByLeft(x):
    return x["location"]['left']


def sortByLeftTop(x):
    return ((-x["location"]['left'],x["location"]['top']))
    


       

json = json.loads(open(r"C:\Users\cbs-shenzhou-001\Desktop\000004.json").read())

words_result = json["data"]["words_result"]


widthAvg = widthAverage(words_result)   #获得识别块平均宽度值（每列宽）

words_result.sort(key =sortByLeft )     #先按识别块左上角起点排序
words_result.reverse()

seeds = words_result[0]["location"]['left'] #定义起始


for i in words_result:      #（按竖行）归并临近块
    location = i["location"]

    left = location['left']
    if (seeds-left)<(widthAvg*0.8):

        i['location']['left'] = seeds
    else:
        seeds = left



words_result.sort(key =sortByLeftTop ) #再次排序，从右到左，从上到下

for i in words_result:
    print(i['words'])
    
    
    
    
