def count_subset_diff(wt,diff):
    l=(sum(wt)+diff)//2
    T=[[False for i in range(l+1)] for i in range(len(wt)+1)]
    return count_subset(wt,len(wt),l,T)

def count_subset(wt,n,W,T):
    for i in range(n+1):
      for j in range(W+1):
         if i==0 and j!=0:
            T[i][j]=0
         elif j==0:
            T[i][j]=1
    for i in range(1,n+1):
       for j in range(1,W+1):
          if i-1>=0:
            if wt[i-1]<=W:
               T[i][j]=T[i-1][j-wt[i-1]]+T[i-1][j]
            elif wt[i-1]>W:
               T[i][j]=T[i-1][j]
    return T[n][W]

if __name__=="__main__":
   print(count_subset_diff([1,2,3,4,10,6,7],2))
   


       
    