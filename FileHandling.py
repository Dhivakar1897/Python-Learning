# Read, Write, update, Delete, Create
'''
x=[2,4,6,5,2,3,8]
for i in x:
    y=i**2
    print(y)

file=open('data1','r')
x=list(file.read())
y=[]
for j in x:
    if j!=',':
        y.append(j)
for i in y:
    print(int(i)**2)
file.close()

a=open("input.py")

print(a.read())
a.close()

a=open('data1','r')
x=list(a.read())
y=[]
for j in x:
    if j!=',':
        y.append(j)
for i in y:
    print(int(i)**2)
'''
a=open('data1','a')
a.write('hello world\n')
a.write('Hi, I am Dhivakar.I am calling from Tamil Nadu.\n')
a.close()
# Delete file
import os
os.remove('data1')
if os.path.exists('data1'):
    os.remove('data1')
else:
    print('file does not exists')