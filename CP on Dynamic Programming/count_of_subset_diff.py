'''
Recursion
'''
def sol(n,sum,arr):
    if sum==0:
        return 1
    if n==0:
        if arr[0]==sum:
            return 1
        return 0
    t=0
    if arr[n]<=sum:
        t=sol(n-1,sum-arr[n],arr)
    nt=sol(n-1,sum,arr)
    return t+nt


arr=[1,1,2,3]
n=len(arr)-1
diff=1
s=sum(arr)
'''
s1-s2=diff ....eq(1)
s1+s2=s ....eq(2)
-------- (Adding eqn 1 and eqn 2)
2s1=s+diff
so, s1=(s+diff)//2

meaning we are reducing this problem to count the subset of sum
'''
if (s + diff) % 2 != 0:
    print(0)  # Not possible
else:
    target = (s + diff) // 2
    print(sol(n, target, arr))
'''
Memoization
'''
def sol(n,sum,arr,dp):
    if sum==0:
        return 1
    if n==0:
        if arr[0]==sum:
            return 1
        return 0
    if dp[n][sum]!=-1:
        return dp[n][sum]
    t=0
    if arr[n]<=sum:
        t=sol(n-1,sum-arr[n],arr,dp)
    nt=sol(n-1,sum,arr,dp)
    dp[n][sum]=t+nt
    return dp[n][sum]


arr=[1,1,2,3]
n=len(arr)-1
diff=1
s=sum(arr)
'''
s1-s2=diff ....eq(1)
s1+s2=s ....eq(2)
-------- (Adding eqn 1 and eqn 2)
2s1=s+diff
so, s1=(s+diff)//2

meaning we are reducing this problem to count the subset of sum
'''
if (s + diff) % 2 != 0:
    print(0)  # Not possible
else:
    target = (s + diff) // 2
    dp=[[-1 for _ in range(target+1)]for _ in range(n+1)]
    print(sol(n, target, arr,dp))