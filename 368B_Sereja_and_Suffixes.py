n, m = map(int, input().split())
nums = list(map(int, input().split()))
prefix = [0] * n
distinct = set()
new = 0
for i in range(n-1, -1, -1):
    if not nums[i] in distinct:
        distinct.add(nums[i])
        new += 1
    prefix[i] = new
 
for _ in range(m):
    l = int(input())
    print(prefix[l-1])