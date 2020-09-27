def count_subset(wt,n,W):
   if n==0 and W!=0:
      return 0
   elif W==0:
      return 1
   if n-1>=0:
      if wt[n-1]<=W:
         return count_subset(wt,n-1,W-wt[n-1])+count_subset(wt,n-1,W)
      else:
         return count_subset(wt,n-1,W)

if __name__=="__main__":
   print(count_subset([2,3,7,6,6],5,12))

   
   