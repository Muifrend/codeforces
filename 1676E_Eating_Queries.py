import bisect

for _ in range(int(input())):
    n, q = map(int, input().split())
    sug_arr = sorted(list(map(int, input().split())), reverse=True)
    
    prefix = [0]*n
    prefix[0] = sug_arr[0]
    for i in range(1,n):
        prefix[i] = sug_arr[i] + prefix[i-1]

    for i in range(q):
        quant = int(input())
        y = bisect.bisect_left(prefix, quant)
        if y == 0:
            print(1)
        elif y>n-1:
            print(-1)
        else: 
            print(y+1)