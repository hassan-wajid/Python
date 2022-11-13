import sys
import copy
listk=[]
n = int(sys.stdin.readline())
for i in range(n):
    listk.append(sys.stdin.readline().rstrip('\n'))

Five_Thousand=5000
One_Thousand=1000
Five_Hundred=500
Two_Hundred=200
One_Hundred=100

Fifty=50
Twenty=20
Ten=10


def declare(Value):
    list=[0 for i in range(8)]
    if(Value<Five_Thousand):
        list[0]="0x5000,"
    if(Value>=Five_Thousand):
        list[0]=str(int(Value/Five_Thousand))+"x5000,"
        Value=Value%Five_Thousand


    if(Value<One_Thousand):
        list[1]="0x1000,"
    if(Value>=One_Thousand):
        list[1]=str(int(Value/One_Thousand))+"x1000,"
        Value=Value%One_Thousand


    if(Value<Five_Hundred):
        list[2]="0x500,"
    if(Value>=Five_Hundred):
        list[2]=str(int(Value/Five_Hundred))+"x500,"
        Value=Value%Five_Hundred



    if(Value<Two_Hundred):
        list[3]="0x200,"
    if(Value>=Two_Hundred):
        list[3]=str(int(Value/Two_Hundred))+"x200,"
        Value=Value%Two_Hundred     



    if(Value<One_Hundred):
        list[4]="0x100,"
    if(Value>=One_Hundred):
        list[4]=str(int(Value/One_Hundred))+"x100,"
        Value=Value%One_Hundred  
 


    if(Value<Fifty):
        list[5]="0x50,"
    if(Value>=Fifty):
        list[5]=str(int(Value/Fifty))+"x50,"
        Value=Value%Fifty

    #print(Value)

    if(Value<Twenty):
        list[6]="0x20,"
    if(Value>=Twenty):
        list[6]=str(int(Value/Twenty))+"x20,"
        Value=Value%Twenty  



    if(Value<Ten):
        list[7]="0x10"
    if(Value>=Ten):
        list[7]=str(int(Value/Ten))+"x10"
        Value=Value%Ten


    return list

#print(declare(4270))

def TrimLeft(list):

    list2=copy.copy(list)
    for i in list:
        #print(list[i])
        #print(list2[i])
        if i[0] =="0":
            list2.remove(i)
            #list=copy.copy(list2)
        else:
            return list2


h=1
for i in listk:
  


    a=declare(int(i))
    b=TrimLeft(a)
    #print(b)
    print("Case #"+str(h)+":",*b)
    h=h+1

#printV(TrimLeft(declare(4270)))

