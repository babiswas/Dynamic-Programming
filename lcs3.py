def lcs(str1,str2,m,n,T):
    if m==0 or n==0:
       return 0
    if T[m][n]!=-1:
        return T[m][n]
    else:
       if str1[m-1]==str2[n-1]:
          T[m][n]=1+lcs(str1,str2,m-1,n-1,T)
       elif str1[m-1]!=str2[n-1]:
          T[m][n]=max(lcs(str1,str2,m,n-1,T),lcs(str1,str2,m-1,n,T))
    return T[m][n]

def lcs_util(str1,str2,m,n):
    T=[[-1 for i in range(n+1)] for i in range(m+1)]
    return lcs(str1,str2,m,n,T)

if __name__=="__main__":
  print(lcs_util("abcdgh","abedfhr",len("abcdgh"),len("abedfhr")))

    