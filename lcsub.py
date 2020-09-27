def lcsub(str1,str2,m,n,T,length):
    for i in range(m+1):
      for j in range(n+1):
         if i==0 or j==0:
            T[i][j]=0
            if length<T[i][j]:
               length=T[i][j]
    for i in range(1,m+1):
      for j in range(1,n+1):
         if str1[i-1]==str2[j-1]:
            T[i][j]=1+T[i-1][j-1]
            if length<T[i][j]:
               length=T[i][j]
         elif str1[i-1]!=str2[j-1]:
             T[i][j]=0
             if length<T[i][j]:
                length=T[i][j]
    return length

def lcsub_util(str1,str2,m,n):
    length=-1
    T=[[-1 for i in range(n+1)] for i in range(m+1)]
    return lcsub(str1,str2,m,n,T,length)

if __name__=="__main__":
   print(lcsub_util("abcde","abfce",len("abcde"),len("abfce")))

   
   