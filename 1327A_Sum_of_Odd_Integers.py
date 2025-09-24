t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    total = 0
    array = []
    if k*k-1< n:
        for i in range(0,k-1):
            total += 2*i+1
            array.append(2*i+1)
        if (n-total)>0 and (n - total) % 2 == 1 and not (n - total) in array :
            print("YES")
        else:
            print("NO")
    else:
        print("NO")