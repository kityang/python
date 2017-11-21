
import os
src = r"/media/abc/D0A2D25DA2D2479C/BaiduNetdiskDownload/剑桥雅思1-9 听力文本+mp3 完整版/剑桥雅思9"

ls = os.listdir(src)
for i in ls:
    old = os.path.join(src,i)
    new = os.path.join(src,"雅思9"+i)
    os.rename(old,new)

