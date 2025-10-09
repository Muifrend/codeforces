import math
n = int(input())
names = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']

k = math.ceil(n/5) + 1
k = math.log(k, 2)
k-= 1
k = math.ceil(k)

s = 5 *(2**k - 1)

i = math.ceil((n-s)/2**k)

print(names[i-1])