'''
Recursion
'''
def soln(n,m,str1,str2):
    if n<0 or m<0:
        return 0
    if str1[n]==str2[m]:
        return 1+soln(n-1,m-1,str1,str2)
    else:
        return max(soln(n,m-1,str1,str2),soln(n-1,m,str1,str2))


class Solution:
    def lcs(self, str1, str2):
      n=len(str1)
      m=len(str2)
      return soln(n-1,m-1,str1,str2)
    
'''
Memoization
'''
def soln(n,m,str1,str2,dp):
    if n<0 or m<0:
        return 0
    if dp[n][m]!=-1:
      return dp[n][m]
    if str1[n]==str2[m]:
        dp[n][m]=1+soln(n-1,m-1,str1,str2,dp)
    else:
        dp[n][m]=max(soln(n,m-1,str1,str2,dp),soln(n-1,m,str1,str2,dp))
    return dp[n][m]

class Solution:
    def lcs(self, str1, str2):
      n=len(str1)
      m=len(str2)
      dp=[[-1 for _ in range(m+1)]for _ in range(n+1)]
      return soln(n-1,m-1,str1,str2,dp)

'''
Tabulation
'''
class Solution:
    def lcs(self, str1, str2):
      n=len(str1)
      m=len(str2)
      dp=[[0 for _ in range(m+1)]for _ in range(n+1)]
      for i in range(1,n+1):
        for j in range(1,m+1):
          if str1[i-1]==str2[j-1]:
            dp[i][j]=1+dp[i-1][j-1]
          else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
      return dp[n][m]