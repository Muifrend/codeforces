n = int(input())
for _ in range(n):
    y = int(input())
    arr = sorted(map(int, input().split()))
    zeroes = arr.count(0)
    one = arr.count(1)
    nOne = arr.count(-1)
    if nOne%2==0:
        print(zeroes)
    else:
        print(zeroes+2)