from collections import Counter

n = int(input())
arr = input().split()
m = int(input()) 
queries = Counter(input().split())

rev_m = m
count = 0
rev_count = 0

for i in range(n):

    count += m
    if queries[arr[i]]:
        m -= queries[arr[i]]
    rev_count += rev_m
    if queries[arr[n-i-1]]:
        rev_m -= queries[arr[n-i-1]]

print(str(count)+' '+str(rev_count))