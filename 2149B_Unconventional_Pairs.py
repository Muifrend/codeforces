n = int(input())
for _ in range(n):
    y = int(input())
    minMax = 0
    arr = sorted(map(int, input().split()))
    for i in range(0,len(arr),2):
        if abs(arr[i]-arr[i+1]) > minMax:
            minMax = abs(arr[i]-arr[i+1])
    print(minMax)