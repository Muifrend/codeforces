import math
n = int(input())

for _ in range(n):
    x, y, k = map(int, input().split())
    x_steps = math.ceil(x/k)
    y_steps = math.ceil(y/k)
    
    if y_steps==x_steps:
        print(y_steps+x_steps)
    elif y_steps>x_steps:
        print(y_steps*2)
    elif x_steps-1==y_steps:
        print(x_steps+y_steps)
    elif x_steps>y_steps:
        print(x_steps*2-1)