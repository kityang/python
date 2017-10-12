import codecs

txt = codecs.open(r"",'w','utf-8')
for i in range(19968,65536):
    txt.write(unichr(i))
    #print unichr(i)
