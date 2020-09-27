def rod_cutting(piece,price,n,l,T):
    for i in range(n+1):
       for j in range(l+1):
          if i==0 and j!=0:
             T[i][j]=0
          elif j==0:
             T[i][j]=0
    for i in range(1,n+1):
       for j in range(1,l+1):
          if i-1>=0:
            if piece[i-1]<=l:
               T[i][j]=max(price[i-1]+T[i][j-piece[i-1]],T[i-1][j])
            elif piece[i-1]>l:
               T[i][j]=T[i-1][j]
    return T[n][l]


def rod_cutting_util(piece,price,n,l):
    T=[[False for i in range(l+1)] for i in range(n+1)]
    return rod_cutting(piece,price,n,l,T)

if __name__=="__main__":
   print(rod_cutting_util(range(1,8),range(1,8),7,7))

   
    
             