"We can convert this problem to subset sum as arr of sum even can be divided into equal sum"

'''
arr=[1,5,11,5]
sum=22 which is even

when can make the question as 

arr=[1,5,11,5]
sum=11 (that is 22/2=11)

if a subset is there then True else False
'''

'''
Recursion
'''
def ps(n,s,arr):
    if n==0:
        return arr[0]==s
    t=False
    if arr[n]<=s:
        t=ps(n-1,s-arr[n],arr)
    nt=ps(n-1,s,arr)
    return t or nt

arr=[1,5,11,5]
s=sum(arr)
if s%2!=0:
    print(False)
else:
    print(ps(len(arr)-1,s//2,arr))


'''
Memoization
'''
def ps(n,s,arr,dp):
    if s==0:
        return True
    if n==0:
        return arr[0]==s
    if dp[n][s]!=-1:
        return dp[n][s]
    t=False
    if arr[n]<=s:
        t=ps(n-1,s-arr[n],arr,dp)
    nt=ps(n-1,s,arr,dp)
    dp[n][s]=t or nt
    return dp[n][s]

arr=[1,5,5]
s=sum(arr)
n=len(arr)-1
if s%2!=0:
    print(False)
else:
    s=s//2
    dp=[[-1 for _ in range(s+1)]for _ in range(n+1)]
    print(ps(n,s,arr,dp))

'''
Tabulation
'''
arr=[1,5,11,5]
s=sum(arr)
n=len(arr)-1
if s%2!=0:
    print(False)
else:
    s=s//2
    dp=[[False for _ in range(s+1)]for _ in range(n+1)]
    for i in range(n+1):
        for j in range(s+1):
            if j==0:
                dp[i][j]=True
    for i in range(1,n+1):
        for j in range(1,s+1):
            t=False
            if arr[i]<=j:
                t=dp[i-1][j-arr[i]]
            nt=dp[i-1][j]
            dp[i][j]=t or nt
    print(dp[n][s])