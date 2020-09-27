def coin_change(coinarr,n,sum,T):
    for i in range(n+1):
       for j in range(sum+1):
          if i==0 and j!=0:
             T[i][j]=0
          elif j==0 and i!=0:
             T[i][j]=1
          elif i==0 and j==0:
             T[i][j]=1
    for i in range(1,n+1):
      for j in range(1,sum+1):
         if i-1>=0:
            if coinarr[i-1]<=j:
               T[i][j]=T[i][j-coinarr[i-1]]+T[i-1][j]
            elif coinarr[i-1]>j:
               T[i][j]=T[i-1][j]
    return T[n][sum]

def coin_change_util(coinarr,n,sum):
    T=[[-1 for i in range(sum+1)] for i in range(n+1)]
    return coin_change(coinarr,n,sum,T)

if __name__=="__main__":
   print(coin_change_util([1,2,3],3,5))

    