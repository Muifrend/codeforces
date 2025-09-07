num = int(input())
charList = list(input())
repeats = 0
for i in range(num-1):
    if charList[i] == charList[i+1]:
        repeats += 1
print(repeats)