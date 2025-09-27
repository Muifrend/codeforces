from collections import Counter
n = int(input())
for _ in range(n):
    k = int(input())
    maximum = k//2
    nums = Counter(list(map(int, input().split())))
    y = nums.most_common(1)[0][1]
    distinct = len(nums.most_common())
    print(y-1) if y==distinct else print(min([distinct, y]))