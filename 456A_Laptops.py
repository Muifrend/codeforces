n = int(input())
y = list(map(int, input().split()))
price, quality = [y[0]],[y[1]]
broke = False
for i in range(1,n):
    k = list(map(int, input().split()))
    if not k[0] == k[1]:
        price.append(k[0])
        quality.append(k[1])
for i in range(len(price)):
    for x in range(len(price)):
        if price[x] < price[i] and quality[x] > quality[i]:
            print('Happy Alex')
            broke = True
            break
    if broke:
        break
if not broke:
    print('Poor Alex') 