# make new array and add old element in new array
from array import *
val = array("i",[10,20,30,40,50])
# copy_array = array(val.typecode,(x for x in val)) # this is normal copy array
copy_array = array(val.typecode,(x*2 for x in val)) # multiplay * 2 array
for i in range (0,len(copy_array)):
    print(copy_array[i],end = " , ")