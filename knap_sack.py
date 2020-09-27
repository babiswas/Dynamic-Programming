def knap_sack(wt,val,n,W):
   if W==0 or n==0:
      return 0
   if n-1>=0:
      if wt[n-1]<=W:
         return max(val[n-1]+knap_sack(wt,val,n-1,W-wt[n-1]),knap_sack(wt,val,n-1,W))
      else:
         return knap_sack(wt,val,n-1,W)

if __name__=="__main__":
   print(knap_sack([10,20,30],[60,100,120],3,50))

