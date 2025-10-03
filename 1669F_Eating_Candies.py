n = int(input())
for _ in range(n):
    k = int(input())
    arr = list(map(int, input().split()))

    prefix_A = k*[0]
    prefix_B = k*[0]
    prefix_A[0] = arr[0] 
    prefix_B[0] = arr[k-1]
    for i in range(1,k):
        prefix_A[i] = prefix_A[i-1] + arr[i]
        prefix_B[i] = prefix_B[i-1] + arr[k-i-1]
    
    set_A = set(prefix_A)
    set_B = set(prefix_B)
    common_nums = list(set_A & set_B)

    mid = sum(arr)//2
    maxi = 0
    for num in common_nums:
        if num<=mid and num>maxi:
            maxi = num
    
    print(prefix_A.index(maxi) + prefix_B.index(maxi)+2) if not maxi == 0 else print(0)