f= open ('twinkel.txt','r')
a = f.read()
if 'twinkel' in a:
    print("twinkel present in file")
else:
    print("not present")
f.close()