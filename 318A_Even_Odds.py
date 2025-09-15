import math
n, k = map(int, input().split())
m = math.ceil(n/2)
print((k-m)*2) if k>m else print(k*2-1)