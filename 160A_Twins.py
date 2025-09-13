n = int(input())
k = input().split()
y = sorted([int(i) for i in k], reverse=True)
minA, sumA, A = sum(y)//2 + 1, 0, 0
while sumA < minA:
    sumA += y[A]
    A += 1 
print(A)