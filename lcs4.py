def lcs(str1,str2,m,n,T):
   for i in range(m+1):
     for j in range(n+1):
         if i==0 or j==0:
            T[i][j]=0
   for i in range(1,m+1):
      for j in range(1,n+1):
          if str1[i-1]==str2[j-1]:
             T[i][j]=1+T[i-1][j-1]
          elif str1[i-1]!=str2[j-1]:
             T[i][j]=max(T[i-1][j],T[i][j-1])
   return T[m][n]

def lcs_util(str1,str2,m,n):
    T=[[-1 for i in range(n+1)] for j in range(m+1)]
    return lcs(str1,str2,m,n,T)

if __name__=="__main__":
    print(lcs_util("abcdgh","abedfhr",len("abcdgh"),len("abedfhr")))

           
        