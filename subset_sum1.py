def subset_sum(wt,n,W,T):
    for i in range(n+1):
      for j in range(W+1):
         if i==0 and j!=0:
             T[i][j]=False
         if j==0:
              T[i][j]=True
    for i in range(1,n+1):
       for j in range(1,W+1):
          if i-1>=0:
            if wt[i-1]<=j:
              T[i][j]=subset_sum(wt,i-1,j-wt[i-1],T) or subset_sum(wt,i-1,j,T)
            elif wt[i-1]>j:
              T[i][j]=subset_sum(wt,i-1,j,T)
    return T[n][W]

def subset_sum_util(wt,n,W):
   T=[[False for i in range(W+1)] for i in range(n+1)]
   return subset_sum(wt,n,W,T)


if __name__=="__main__":
   print(subset_sum_util([2,3,7,6,6],5,12))

   
   