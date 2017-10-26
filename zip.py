import os
import zipfile

src = r"F:\册）"
dst = r"G:\真"

ls = os.listdir(src)

for i in ls:
    zipPath = os.path.join(src,i)
    dstpath = os.path.join(dst,i).replace(".zip","")
    if not os.path.exists(dstpath):
        os.makedirs(dstpath)
    

    f = zipfile.ZipFile(zipPath,'r')
    for pdg in f.namelist():
        f.extract(pdg,dstpath)
    
