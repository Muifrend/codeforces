import math
n = int(input())
for _ in range(n):
    y = int(input())
    y_root = math.ceil(y**(1/3))
    flag = False
    for b in range(1, y_root):
        a = round((y - b**3)**(1/3),11)
        a_rounded = round(a)
        if a == a_rounded:
            flag = True
            break
    print('YES') if flag else print('NO')