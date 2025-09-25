from collections import Counter
n = int(input())
first = Counter(input().split())
second = Counter(input().split())
third = Counter(input().split())
out1 = list((first-second).elements())[0]
out = list((first - third).elements())
if out[0] == out1:
    print(out[0])
    print(out[1])
else:
    print(out[1])
    print(out[0])