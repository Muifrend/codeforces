x = 0
y = 0
for i in range(5):
    n = input().split()
    if "1" in n:
        x = i
        y = n.index("1")
print(abs(int(x)-2)+abs(int(y)-2))