k = int(input())
m, c = 18, 0
while not c == k:
    m+=1
    n = m
    s = 0
    while n>0:
        s += n%10
        n = n//10
    if s == 10:
        c+=1
print(m)