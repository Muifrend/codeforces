t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    low, high = 1, max(a) + x
    ans = 1
    while low <= high:
        mid = (low + high) // 2
        water_needed = sum(max(0, mid - height) for height in a)
        if water_needed <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    print(ans)