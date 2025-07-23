'''
Recursion
'''
def sol(n,s,arr):
    if s==0:
        return 1
    if n==0:
        if arr[0]==s:
            return 1
        return 0
    t=0
    if arr[n]<=s:
        t=sol(n-1,s-arr[n],arr)
    nt=sol(n-1,s,arr)
    return t+nt

arr=[2,3,5,6,8]
s=10
n=len(arr)-1
print(sol(n,s,arr))

'''
Memoization
'''
def sol(n,s,arr,dp):
    if s==0:
        return 1
    if n==0:
        if arr[0]==s:
            return 1
        return 0
    if dp[n][s]!=-1:
        return dp[n][s]
    t=0
    if arr[n]<=s:
        t=sol(n-1,s-arr[n],arr,dp)
    nt=sol(n-1,s,arr,dp)
    dp[n][s]=t+nt
    return dp[n][s]

arr=[2,3,5,6,8,10]
s=10
n=len(arr)-1
dp=[[-1 for _ in range(s+1)]for _ in range(n+1)]
print(sol(n,s,arr,dp))

'''
Tabulation
'''
arr=[2,3,5,6,8]
s=10
n=len(arr)-1
dp=[[0 for _ in range(s+1)]for _ in range(n+1)]
for i in range(n+1):
    dp[i][0]=1
    
# base condition like arr[0]=2 then we have intialize in the dp[0][2]=1
if arr[0] <= s:
    dp[0][arr[0]] = 1
print(dp)
for i in range(1,n+1):
    for j in range(1,s+1):
        t=0
        if arr[i]<=j:
            t=dp[i-1][j-arr[i]]
        nt=dp[i-1][j]
        dp[i][j]=nt+t
print(dp[n][s])