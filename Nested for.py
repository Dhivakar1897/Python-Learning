# Nested for loop
'''
*
**
***
****
*****
'''
for i in range(6):
    for j in range(i):
        print("*",end="")
    print("")
print("-------------")
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("")
print("-------------")
for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print("")
print("-------------")
for i in range(5):
    for j in range(97,102,1):
        print(chr(j),end="")
    print("")
print("-------user----------")
a=int(input("Enter The Number:"))
for i in range(a+1):
    for j in range(i):
        print("*",end="")
    print()
print("-------user----------")
a=int(input("Enter The Number:"))
for i in range(a,0,-1):
    for j in range(i):
        print("*",end="")
    print()