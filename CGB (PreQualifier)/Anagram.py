import string
import sys
import copy
listk=[]
n = int(sys.stdin.readline())
for i in range(n*2):
    listk.append(sys.stdin.readline().rstrip('\n'))

#print(listk)
def checkAnagram(string1,string2):
    string1=sorted(string1.replace(" ", ""))
    string2=string2.replace(" ","")
    delta=True
    if len(string2) <len(string1):
            for i in string2:
                if (i in string1):
                    string1.remove(i)
                else:
                    delta=False
                    #print(i)
                    return "Not Possible"

                
            return "Possible"
    else :
        return "Not Possible"


for i in range(0,n+1,2):
    #print(i)
    string1=listk[i]
    string2=listk[i+1]

    #print(string1,string2)
    print(checkAnagram(string1=string1,string2=string2))



#print(checkAnagram("it is cold","driving car"))

