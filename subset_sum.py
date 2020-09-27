def knapsack(wt,n,W):
   if n==0 and W!=0:
      return False
   elif W==0:
      return True
   if n-1>=0:
      if wt[n-1]<=W:
         return (knapsack(wt,n-1,W-wt[n-1])) or (knapsack(wt,n-1,W))
      elif wt[n-1]>W:
         return (knapsack(wt,n-1,W))

if __name__=="__main__":
   print(knapsack([2,3,7,8,10],5,11))


      