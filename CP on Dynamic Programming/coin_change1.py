'''
Recursion
'''
def soln(n,s,coin):
    if n==0:
        return 1 if s%coin[0]==0 else 0
    if s==0:
        return 1
    t=0
    if coin[n]<=s:
        t=soln(n,s-coin[n],coin)
    nt=soln(n-1,s,coin)
    return t+nt

coin=[1,2,3]
s=5
n=len(coin)-1
print(soln(n,s,coin))

'''
Memoization
'''
def soln(n,s,coin,dp):
    if n==0:
        return 1 if s%coin[0]==0 else 0
    if s==0:
        return 1
    if dp[n][s]!=-1:
        return dp[n][s]
    t=0
    if coin[n]<=s:
        t=soln(n,s-coin[n],coin,dp)
    nt=soln(n-1,s,coin,dp)
    dp[n][s]=t+nt
    return dp[n][s]

coin=[1,2,3]
s=5
n=len(coin)-1
dp=[[-1 for _ in range(s+1)]for _ in range(n+1)]
print(soln(n,s,coin,dp))

'''
Tabulation
'''
coin=[1,2,3]
s=5
n=len(coin)-1
dp=[[0 for _ in range(s+1)]for _ in range(n+1)]

for i in range(n+1):
    dp[i][0]=1
for j in range(s+1):
    dp[0][j]=1 if s%coin[0]==0 else 0
for i in range(1,n+1):
    for j in range(1,s+1):
        t = 0
        if coin[i]<=j:
            t=dp[i][j-coin[i]]
        nt=dp[i-1][j]
        dp[i][j]=t+nt
print(dp[n][s])