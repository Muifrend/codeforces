for _ in range(int(input())):
    n, c = map(int, input().split())
    s_arr = list(map(int, input().split()))
    suar = sum(s_arr)
    s_sq_arr = [x**2 for x in s_arr]
    k = c-sum(s_sq_arr)

    high = k
    low = 1
    mid = 0

    while True:
        mid = low + (high - low) // 2  
        sim = n*mid**2 + 2*mid*suar
        if sim == k:
            print(mid//2)
            break
        if sim < k:
            low = mid + 1
        else:
            high = mid - 1 