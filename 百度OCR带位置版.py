import os
from PIL import Image,ImageDraw,ImageFont
import xlrd

def drawLine(left,top,width,height):
    ls = [1]*4
    ls[0] = (left,top,left,top+height)
    ls[1] = (left,top,left+width,top)
    ls[2] = (left+width,top,left+width,top+height)
    ls[3]= (left,top+height,left+width,top+height)

    return ls
    


src = r"C:\Users\ygl\Desktop\000004原图.jpg"
excel = xlrd.open_workbook(r"C:\Users\ygl\Desktop\000004.xls")
img = Image.open(src)

drawImg = ImageDraw.Draw(img)

sheet = excel.sheets()[0]

nrows = sheet.nrows
ncols = sheet.ncols

for i in range(nrows):
    loctionNum = sheet.cell(i,0).value
    left = sheet.cell(i,2).value
    top = sheet.cell(i,3).value
    width = sheet.cell(i,4).value
    height = sheet.cell(i,5).value
    
    lines = drawLine(left,top,width,height)
    drawImg.line(lines[0],fill="green")
    drawImg.line(lines[1],fill="green")
    drawImg.line(lines[2],fill="green")
    drawImg.line(lines[3],fill="green")

    boxCenter =((left*2+width-15)/2,(top*2+height)/2)
    Font = ImageFont.truetype("C:\Windows\Fonts\simsunb.ttf",24)
    drawImg.text(boxCenter,str(int(loctionNum)),'red',font=Font)

img.show()

img.save(r"C:\Users\ygl\Desktop\000005.jpg")
    
    
    
