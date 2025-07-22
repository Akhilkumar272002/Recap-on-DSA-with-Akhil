'''
Recursion
'''
def ss(n,sum,arr):
    if sum==0:
        return True
    if n==0:
        return arr[0]==sum
    take=False
    if arr[n]<=sum:
        take=ss(n-1,sum-arr[n],arr)
    nt=ss(n-1,sum,arr)
    return take or nt

arr=[2,3,7,8,10]
sum=11
n=len(arr)-1
print(ss(n,sum,arr))

'''
Memoization
'''
def ss(n,sum,arr,t):
    if sum==0:
        return True
    if n==0:
        return arr[n]==sum
    if t[n][sum]!=-1:
        return t[n][sum]
    take=False
    if arr[n]<=sum:
        take=ss(n-1,sum-arr[n],arr,t)
    nt=ss(n-1,sum,arr,t)
    t[n][sum]=take or nt
    return t[n][sum]

arr=[2,3,7,8,10]
sum=11
n=len(arr)-1
t=[[-1 for i in range(sum+1)]for i in range(n+1)]
print(ss(n,sum,arr,t))

'''
Tabulation
'''
arr=[2,3,7,8,10]
sum=11
n=len(arr)-1
t=[[False for i in range(sum+1)]for j in range(n+1)]
for i in range(n+1):
    for j in range(sum+1):
        if j==0:
            t[i][j]=True
            
for i in range(1,n+1):
    for j in range(1,sum+1):
        take=False
        if arr[i]<=j:
            take=t[i-1][j-arr[i]]
        nt=t[i-1][j]
        t[i][j]=take or nt

print(t[n][sum])

