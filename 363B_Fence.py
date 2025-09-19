n, k = map(int, input().split())
fence = list(map(int, input().split()))
sumAmount = sum(fence[0:k])
minAmount = sumAmount
index = 0
for i in range(1,n-k+1):
    sumAmount = sumAmount - fence[i-1] + fence[i+k-1]
    if minAmount > sumAmount:
        minAmount = sumAmount
        index = i
print(index+1)