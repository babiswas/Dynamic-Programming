def lcs(str1,str2):
   if len(str1)==0 or len(str2)==0:
      return 0
   elif str1[len(str1)-1]==str2[len(str2)-1]:
        return 1+lcs(str1[0:len(str1)-1],str2[0:len(str2)-1])
   elif str1[len(str1)-1]!=str2[len(str2)-1]:
        return max(lcs(str1,str2[0:len(str2)-1]),lcs(str1[0:len(str1)-1],str2))

if __name__=="__main__":
   print(lcs(list("abcdgh"),list("abedfhr")))
