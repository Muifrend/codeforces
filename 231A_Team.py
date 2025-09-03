n = int(input())
counter = 0
for i in range(n):
    counter2 = 0
    li = input().split()
    for y in li:
        counter2 += int(y)
    if counter2>1:
            counter+=1           
print(counter)