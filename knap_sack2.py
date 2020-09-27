def knapsack_util(wt,val,n,W,T):
   if n==0 or W==0:
      T[n][W]=0
      return 0
   if n-1>=0:
      if T[n-1][W]!=-1:
         return T[n-1][W]
      else:
         if wt[n-1]<=W:
            T[n-1][W]=max(val[n-1]+knapsack_util(wt,val,n-1,W-wt[n-1],T),knapsack_util(wt,val,n-1,W,T))
         elif wt[n-1]>W:
            T[n-1][W]=knapsack_util(wt,val,n-1,W,T)
         return T[n-1][W]

def knap_sack(wt,val,n,W):
   T=[[-1 for i in range(W+1)] for i in range(n+1)]
   return knapsack_util(wt,val,n,W,T)

if __name__=="__main__":
   print(knap_sack([10,20,30],[60,100,120],3,50))
   