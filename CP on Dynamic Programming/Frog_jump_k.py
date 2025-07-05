'''
Recursion code
'''
def frog_jump(indx, arr, k):
    if indx==0:
        return 0
    ans=float('inf')
    for i in range(1,k):
        if indx-i>=0:
            jump=frog_jump(indx-i,arr,k)+abs(arr[indx]-arr[indx-i])
            ans=min(ans,jump)
    return ans

arr=[10,20,30,10]
k=3
print(frog_jump(len(arr)-1,arr,k))

'''
Memorization Code
'''
def frog_jump(indx, arr, k,dp):
    if indx==0:
        return 0
    if dp[indx]!=-1:
        return dp[indx]
    ans=float('inf')
    for i in range(1,k):
        if indx-i>=0:
            jump=frog_jump(indx-i,arr,k,dp)+abs(arr[indx]-arr[indx-i])
            ans=min(ans,jump)
    dp[indx]=ans
    return dp[indx]

arr=[10,20,30,10]
k=3
dp=[-1 for i in range(len(arr))]
print(frog_jump(len(arr)-1,arr,k,dp))

'''
Tabulation Code
'''

arr=[10,20,30,10]
k=3
print(frog_jump(len(arr)-1,arr,k))

dp[0]=0
for i in range(1, len(arr)):
    ans=float('inf')
    for j in range(1,k+1):
        if i-j>=0:
            jump=dp[i-j]+abs(arr[i]-arr[i-j])
            ans=min(ans,jump)
    dp[i]=ans

print(dp[len(arr)-1])