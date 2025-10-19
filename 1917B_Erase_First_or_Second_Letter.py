for _ in range(int(input())):
    n = int(input())
    s = input()
    d = set(s[0])
    c = 1
    for i in range(1,n):
        d.add(s[i])
        c += len(d)
    print(c)    