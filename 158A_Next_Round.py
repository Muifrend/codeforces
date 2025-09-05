n = input().split()
counter = 0
k = int(n[1])
y = input().split()
for i in y:
    if int(i)>0 and int(i)>int(y[k-1])-1:
        counter+=1
print(counter)