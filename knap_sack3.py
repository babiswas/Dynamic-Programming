def knapsack_util(wt,val,n,W,T):
    for i in range(n+1):
       for j in range(W+1):
          if i==0 or j==0:
              T[i][j]=0
    for i in range(1,n+1):
       for j in range(1,W+1):
            if i-1>=0:
               if wt[i-1]<=j:
                  T[i][j]=max(val[i-1]+T[i-1][j-wt[i-1]],T[i-1][j])
               elif wt[i-1]>j:
                  T[i][j]=T[i-1][j]
    return T[n][W]

def knap_sack(wt,val,n,W):
   T=[[-1 for i in range(W+1)] for j in range(n+1)]
   return knapsack_util(wt,val,n,W,T)

if __name__=="__main__":
   print(knap_sack([10,20,30],[60,100,120],3,50))
