'''
Recursion
'''
def knapsack(indx,W,wt,val):
    if indx==0 or W==0:
        return 0
    take=float('-inf')
    if W-wt[indx]>=0:
        take=val[indx]+knapsack(indx-1,W-wt[indx],wt,val)
    nottake=knapsack(indx-1,W,wt,val)
    return max(take,nottake)

wt=[1,3,4,5]
val=[1,4,5,7]
W=7
print(knapsack(len(wt)-1,W,wt,val))


'''s
Memoization
'''
def knapsack(indx, W, wt, val, t):
    if indx == 0 or W == 0:
        return 0
    if t[indx][W] != -1:
        return t[indx][W]
    
    take = float('-inf')
    if wt[indx - 1] <= W:
        take = val[indx - 1] + knapsack(indx - 1, W - wt[indx - 1], wt, val, t)
    
    nottake = knapsack(indx - 1, W, wt, val, t)
    t[indx][W] = max(take, nottake)
    return t[indx][W]

wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 7
n = len(wt)
t = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

print(knapsack(n, W, wt, val, t))

'''
Tabulation
'''
wt=[1,3,4,5]
val=[1,4,5,7]
W=7
t=[[-1 for i in range(W+1)]for j in range(len(wt)+1)]
for i in range(len(wt)+1):
    for j in range(W+1):
        if i==0 or j==0:
            t[i][j]=0
for i in range(1,len(wt)+1):
    for j in range(1,W+1):
        ta=float('-inf')
        if wt[i-1]<=j:
            ta=val[i-1]+t[i-1][j-wt[i-1]]
        nt=t[i-1][j]
        t[i][j]=max(ta,nt)
print(t[len(wt)][W])
