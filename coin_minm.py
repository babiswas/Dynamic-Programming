import sys

INT_MAX=sys.maxsize

def min_coin(coinarr,n,sum,T):
    for i in range(n+1):
       for j in range(sum+1):
          if i==0 and j!=0:
             T[i][j]=INT_MAX-1
          elif i!=0 and j==0:
             T[i][j]=0
          elif i==0 and j==0:
             T[i][j]=0
    for j in range(1,sum+1):
       if j%coinarr[0]==0:
          T[1][j]=j//coinarr[0]
       else:
          T[1][j]=INT_MAX-1
    for i in range(2,n+1):
       for j in range(1,sum+1):
          if i-1>=0:
            if coinarr[i-1]<=j:
               T[i][j]=min(1+T[i][j-coinarr[i-1]],T[i-1][j])
            else:
               T[i][j]=T[i-1][j]
    return T[n][sum]


def min_coin_util(coinarr,n,sum):
    T=[[-1 for i in range(sum+1)] for j in range(n+1)]
    return min_coin(coinarr,n,sum,T)



if __name__=="__main__":
   print(min_coin_util([1,2,3],3,5))


   

          
          
    
          
          
    