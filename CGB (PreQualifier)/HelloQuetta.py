import sys
list=[]
n = int(sys.stdin.readline())
for i in range(n):
    list.append(sys.stdin.readline().rstrip('\n'))
    

for i in list:
     sys.stdout.write("Hello "+i+"!\n")


 

     