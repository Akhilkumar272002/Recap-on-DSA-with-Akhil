'''
Recursion
'''
def soln(n,W,wt,val):
    if n==0:
        return int((W/wt[0])*val[0])
    t=float('-inf')
    if wt[n-1]<=W:
        t=val[n-1]+soln(n,W-wt[n-1],wt,val)
    nt=soln(n-1,W,wt,val)
    return max(nt,t)

wt = [2, 4, 6]
val = [5, 11, 13]
W = 10
n = len(wt)-1
print(soln(n,W,wt,val))

'''
Memoization
'''
def soln(n,W,wt,val,dp):
    if n==0:
        return (W//wt[0])*val[0]
    if dp[n][W]!=-1:
        return dp[n][W]
    t=float('-inf')
    if wt[n]<=W:
        t=val[n]+soln(n,W-wt[n],wt,val,dp)
    nt=soln(n-1,W,wt,val,dp)
    dp[n][W]=max(nt,t)
    return dp[n][W]

wt = [2, 4, 6]
val = [5, 11, 13]
W = 10
n = len(wt)-1
dp=[[-1 for _ in range(W+1)]for _ in range(n+1)]
print(soln(n,W,wt,val,dp))

'''
Tabulation
'''
# def soln(n,W,wt,val,dp):
#     if n==0:
#         return (W//wt[0])*val[0]
#     if dp[n][W]!=-1:
#         return dp[n][W]
#     t=float('-inf')
#     if wt[n]<=W:
#         t=val[n]+soln(n,W-wt[n],wt,val,dp)
#     nt=soln(n-1,W,wt,val,dp)
#     dp[n][W]=max(nt,t)
#     return dp[n][W]
#
wt = [2, 4, 6]
val = [5, 11, 13]
W = 10
n = len(wt)-1
dp=[[0 for _ in range(W+1)]for _ in range(n+1)]

for i in range(W+1):
    dp[0][i]=(i//wt[0])*val[0]
for i in range(1,n+1):
    for j in range(1,W+1):
        t=float('-inf')
        if wt[i]<=j:
            t=val[i]+dp[i][j-wt[i]]
        nt=dp[i-1][j]
        dp[i][j]=max(t,nt)
print(dp[n][W])