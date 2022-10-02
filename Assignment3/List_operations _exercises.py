#List operations exercises
import numpy as np
numlist=[1,2,3]
print(numlist*2) #print list twice

numarr=np.array([1,2,3])
print(numarr*2)
#each object in the array is multiple by 2

strlist=['do','re','mi','fa']
print([strlist[0]*2+"",strlist[1]*2+"",strlist[2]*2+"",strlist[3]*2+""])
print(strlist*2)
print([strlist[0],strlist[0],strlist[1],strlist[1],
    strlist[2],strlist[2],strlist[3],strlist[3]])

print([[strlist[0],strlist[0]],[strlist[1],strlist[1]],
    [strlist[2],strlist[2]],[strlist[3],strlist[3]]])
