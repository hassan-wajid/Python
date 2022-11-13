import sys
list=[]
n = int(sys.stdin.readline())
for i in range(n):
    list.append(sys.stdin.readline().rstrip('\n'))

value=0
def IfPrime(num):# Program to check if a number is prime or not

    flag = False

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break

    # check if flag is True
    if flag:
        return False
    else:
        return True
a=1
for i in list:
  
    i=[int(x) for x in i.split(' ')]
    if(IfPrime(i[0]) and IfPrime(i[1])):
        value=i[0]+i[1]

    elif(IfPrime(i[0]) or IfPrime(i[1])):
        value=i[0]*i[1]
    else:
        value="Not possible"

    print("Case #"+str(a)+": "+str(value))
    a=a+1

    