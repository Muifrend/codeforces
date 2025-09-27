n, m, k = map(int, input().split())
array = []
num = 0
for _ in range(m+1):
    bi = bin(int(input()))[2:]
    array.append((n-len(bi))*'0'+bi)
fedor = array.pop()
for i in array:
    counter = 0
    for y in range(n-1,-1,-1):
        if not i[y]==fedor[y]:
            counter+=1
    if counter<=k:
        num+=1
print(num)