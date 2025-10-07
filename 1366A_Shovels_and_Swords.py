n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    e = 0
    while a>0 and b>0:

        dif = abs(a-b)
        if dif%2 ==1:
            dif-=1

        if a == b or dif==0:
            e += (b+a)//3
            break
        elif a>b:
            a-=dif
            e+= min(dif//2,b)
            b-=dif//2
        else:
            b-=dif
            e+=min(dif//2,a)
            a-=dif//2
            
    print(e)