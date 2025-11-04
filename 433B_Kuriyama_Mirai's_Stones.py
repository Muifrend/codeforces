n = int(input())
arr_v = list(map(int, input().split()))
arr_u = sorted(arr_v)
 
for _ in range(int(input())):
    tp, l, r = map(int, input().split())
    if tp == 1:
        print(sum(arr_v[l-1:r]))
    else:
        print(sum(arr_u[l-1:r]))