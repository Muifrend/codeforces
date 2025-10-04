n = int(input())

def total(i):
    if i in memo:
        return memo[i]
    if i+arr[i]>=len(arr):
        return arr[i]
    memo[i] = total(i+arr[i]) + arr[i]
    return memo[i]

for _ in range(n):
    memo = {}
    y = int(input())
    arr = list(map(int, input().split()))
    high, curr = 0, 0
    for i in range(y-1, -1, -1):
        curr = total(i)
        if curr>high:
            high = curr
    print(high)