# make a empty array and add element in user 
from array import *
val = array("i",[])
n = int(input("enter the index so which element added ="))
for i in range(0,n):
    a = int(input("enter the element="))
    val.append(a)

for x in val:
    print(x,end=" ")
    
    