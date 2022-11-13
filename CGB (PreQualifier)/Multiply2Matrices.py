
list1=[]
n = int(input().strip())
for i in range(n):
    list1.append(input().strip().split(" "))


def MakeMatrix(x):
    #Do not pass array as a string !!
    MatrixOneDim=x[:2]
    MatrixOne=x[2:(MatrixOneDim[1]*MatrixOneDim[0])+2]
    MatrixTwoDim=x[(MatrixOneDim[1]*MatrixOneDim[0])+2:(MatrixOneDim[1]*MatrixOneDim[0])+4]
    MatrixTwo=x[(MatrixOneDim[1]*MatrixOneDim[0])+4:]
    #print("mat1 dim",MatrixOneDim,"mat 2 dim",MatrixTwoDim)
    if MatrixOneDim[1]!=MatrixTwoDim[0] and MatrixOneDim[1]!=MatrixTwoDim[1]:
        return 0,0
    mat1 = converToMatrix(MatrixOne,MatrixOneDim)
    mat2 = converToMatrix(MatrixTwo,MatrixTwoDim)
    if MatrixOneDim[1]!=MatrixTwoDim[0] and MatrixOneDim[1]==MatrixTwoDim[1]:
        mat1=Transpose(mat1)
    return mat1,mat2


def converToMatrix(array,Dim):
    mat1 = []
    while array != []:
            mat1.append(array[:Dim[1]])
            array = array[Dim[1]:]
    return mat1


def Transpose(array):
    #problem
    return [list(x) for x in zip(*array)]


def multiplication(Mat1,Mat2):
    # iterate through rows of X
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Mat2)] for X_row in Mat1]   
    return result

#list1=[[2 ,3 ,1 ,2 ,3 ,4 ,5 ,6 ,1 ,4 ,1 ,2 ,3 ,4],[3 ,4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 3 ,4, 1, 0, 3, 4, 5, 6, 1, 8, 0, 0, 0, 12]]
alpha=True
h=1
for i in list1:
   
    alpha=True
    d=[int(x) for x in i]
    a,b=MakeMatrix(d)
    #print("asdadasd",a,b)
    if a==0 and b==0 :

        print("Case #"+str(a)+": Not possible")
        alpha=False
        h=h+1
    else:
        if alpha==True:
            #print(sum([sum(x)  for x in multiplication(a,b)]))
            print("Case #"+str(h)+": "+str(sum([sum(x)  for x in multiplication(b,a)])))
            h=h+1


    
    
    
    

#d = [3 ,4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 3 ,4, 1, 0, 3, 4, 5, 6, 1, 8, 0, 0, 0, 12]
#d=['3' ,'4', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '3' ,'4', '1',' 0', '3', '4', '5', '6', '1', '8', '0',' 0', '0', '12']
#a,b=MakeMatrix(d)

#print(sum([sum(x)  for x in multiplication(b,a)]))