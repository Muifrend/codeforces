n = int(input())
counter = 0
for i in range(n):
    y = input()
    if "++" in y:
        counter+=1
    if "--" in y:
        counter-=1
print(counter)