
import sys
import copy
list=[]
n = int(input().strip())
for i in range(n):
    list.append(input().strip().split(" "))

#print(list[0])

def function(list):
    MainList=copy.copy(list)
    TempMax=[]
    while(len(MainList)>0):
        NewList=[]
        TempList=copy.copy(MainList)
        while(len(TempList)>0):
            b=min(TempList)
            tempMinIndex = TempList.index(min(TempList))
            MainList.remove(b)
            if len(TempList)>1:
                TempList=TempList[tempMinIndex+1:]
            else :
                TempList=[]
            NewList.append(b)
            
        if len(TempMax)<len(NewList):
            TempMax=NewList[:]
        

    return TempMax


for i in list:
    a=1
    i=[int(j) for j in i]

    MaxStudent=function(i)
    
    
    print("Case #"+str(a)+": "+str(len(MaxStudent)),*MaxStudent)
    a=a+1





#print(n)
#print(list)