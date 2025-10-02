n = int(input())
for _ in range(n):
    y = int(input())
    pairs = sorted(list(map(int, input().split())))
    odd, subsequent = 0, 0

    for i in range(y):
        if pairs[i]%2 == 1:
            odd += 1
        if i<y-1 and pairs[i]+1 == pairs[i+1]:
            subsequent += 1
    
    print('NO') if odd%2==1 and not subsequent else print('YES')