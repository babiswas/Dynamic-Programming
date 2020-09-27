def min_sub_sum_diff(wt):
    n=len(wt)
    W=sum(wt)
    minm=W+1
    T=[[False for i in range(W+1)] for i in range(n+1)]
    subset_sum(wt,n,W,T)
    for i in range((W//2)+1):
       if T[n][i]:
          val=W-2*i
       if minm>val:
          minm=val
    return minm
          
    
def subset_sum(wt,n,W,T):
    for i in range(n+1):
      for j in range(W+1):
         if i==0 and j!=0:
            T[i][j]=False
         elif j==0:
            T[i][j]=True
    for i in range(1,n+1):
       for j in range(1,W+1):
          if i-1>=0:
             if wt[i-1]<=W:
                T[i][j]=T[i-1][j-wt[i-1]] or T[i-1][j]
             elif wt[i-1]:
                T[i][j]=T[i-1][j]

if __name__=="__main__":
   print(min_sub_sum_diff([1,2,7]))
   


