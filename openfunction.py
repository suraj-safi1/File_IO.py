f=open('sample.txt','r')
data = f.read()
print(data)
data1=f.read(5)
print(data1)
'''
data=f.readline()
print(data)'''
f.close()