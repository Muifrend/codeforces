n = int(input())
bills = list(map(int, input().split()))
hasBill = True
counter = 0
cash = 3*[0]

while hasBill and counter<n:
    if bills[counter] == 25:
        cash[0]+=1
    elif bills[counter] == 50 and cash[0] > 0:
        cash[1]+=1
        cash[0]-=1
    elif bills[counter] == 100 and cash[1]>0 and cash[0]>0:
        cash[2]+=1
        cash[1]-=1
        cash[0]-=1
    elif bills[counter] == 100 and cash[0]>2:
        cash[2]+=1
        cash[0]-=3
    else:
        hasBill = False
    counter+=1

print('YES') if hasBill else print('NO')