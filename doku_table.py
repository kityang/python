#!python2
#coding:utf8
'''
将xls表格内容转换为dokuwiki格式
'''
import os
import xlrd

excel = xlrd.open_workbook(r"/home/abc/Desktop/test.xls")
txt = open(r"/home/abc/Desktop/dktableresult.txt","w")

sheet = excel.sheets()[0]

nrows = sheet.nrows
ncols = sheet.ncols

for i in range(0,nrows):
    line = "|"
    for j in range(0,ncols):
        line = line +"  "+sheet.cell(i,j).value +"  |"
    txt.write(line.encode("utf8"))

txt.close()
print "转换完毕"


