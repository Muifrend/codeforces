numbers = input().split()
minStages = int(numbers[1])
string = input()
sortedString = sorted(set(list(string)))
size = len(sortedString)
alphabet = list('abcdefghijklmnopqrstuvwxyz')
counter = 0
weight = 0
stages = 0
for i in range(26):
    if stages == minStages:
        break
    if counter<size:
        if alphabet[i] == sortedString[counter]:
            weight += i+1
            stages += 1
            if i+1<26 and counter+1<size:
                if alphabet[i+1] == sortedString[counter+1]:
                    sortedString.pop(counter+1)
                    size -= 1
            counter += 1          
if int(numbers[1])>len(sortedString):
    print(-1)
else:
    print(weight)