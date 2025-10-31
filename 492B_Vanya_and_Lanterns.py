n, l = map(int, input().split())
s = set(map(int, input().split()))
arr = sorted(list(s))
min_d = 0

for i in range(len(arr)-1):
    d = abs(arr[i] - arr[i+1])/2
    if min_d<d:
        min_d = d
        
d = arr[0] 
if d > min_d:
    min_d = d
    
d = ((l-arr[len(arr)-1]))
if d > min_d:
    min_d = d

print(min_d)