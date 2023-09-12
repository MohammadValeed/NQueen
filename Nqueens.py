from math import *
x={}
n=4

def place(k,i):
    if(i in x.values()):
        return False
    j=1
    while j<k:
        a=x[j]
        if abs(n-i)==abs(j-k):
            return False
        j=j+1
    return True

def clearBlocks(k):
    for i in range(k,n+1):
        x[i]=None
        
def Nqueens(k):
    for i in range(1,n+1):
        clearBlocks(k):
            if place(k,i):
                x[k]=i
                if k==n:
                    for j in x:
                        print("Place Queen in position: ",x[j])
                    print("-----------------------")
            
                else:
                    Nqueens(k+1)
                    
Nqueens(1)