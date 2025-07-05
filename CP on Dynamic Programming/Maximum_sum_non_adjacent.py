''''
can be done using simple take and not take method as subsequences
'''

'''
Recursion code
'''
def sol(indx, arr):
    if indx == 0:
        return arr[indx]
    if indx < 0: return 0
    ans = float('-inf')
    for i in range(1, indx + 1):
        if indx - i >= 0 and indx - 1 != indx - i:
            adj = arr[indx] + sol(indx - i, arr)
            ans = max(ans, adj)
    return ans

arr=[2,1,4,9]
print(sol(len(arr)-1,arr))

'''
Memorization code
'''
def sol(indx, arr, dp):
    if dp[indx] != -1:
        return dp[indx]
    if indx == 0:
        return arr[indx]
    if indx < 0: return 0
    ans = float('-inf')
    for i in range(1, indx + 1):
        if indx - i >= 0 and indx - 1 != indx - i:
            adj = arr[indx] + sol(indx - i, arr, dp)
            ans = max(ans, adj)
    dp[indx] = ans
    return dp[indx]

arr=[2,1,4,9]
dp=[-1 for i in range(len(arr))]
print(sol(len(arr)-1,arr,dp))

'''
Tabulation code
'''
arr=[2,1,4,9]
dp=[-1 for i in range(len(arr))]

dp[0]=arr[0]
neg=0
for i in range(1,len(arr)):
    ans=float('-inf')
    for j in range(1,i+1):
        if i - j >= 0 and i - 1 != i - j:
            adj = arr[i] + dp[i - j]
            ans = max(ans, adj)
    dp[i]=ans
print(dp[len(arr)-1])