s = list(input())
n = int(input())
length = len(s)
prefix = [0] * length
 
for i in range(1, length):
    prefix[i] = prefix[i-1] + (1 if s[i-1]==s[i] else 0)
 
for _ in range(n):
    l,r = map(int, input().split())
    print(prefix[r-1] - prefix[l-1])