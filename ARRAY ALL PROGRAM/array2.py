# In a sortcut array import 
from array import *
val = array ("i", [ 1,2,3,4,5,6,7])
for i in range (0,len(val)):  # len = length of array
    #print(i,end=" ")
#print(val.typecode) # type of array
    
    
    # typecode   -   python datatype  -    byte size
    #    i                  int                2
    #    I                  int                2
    #    u             unicode char            2
    #    h                  int                2
    #    H                  int                2 
    #    l                  int                4
    #    L                  int                4 
    #    f                 float               4
    #    d                 float               8
    
    print(val[i],end=" ")
    