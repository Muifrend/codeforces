for _ in range(int(input())):
    a, b, x, y, n = map(int, input().split())

    dic = {
        x: 'a1',
        (a-n): 'a2',
        y: 'b1',
        (b-n): 'b2', 
    }
    
    val = dic[min(max(x,a-n),max(y,b-n))]
    
    if a-x+b-y<n:
        print(x*y)
    elif val == 'a2':
        print((a-n)*b)
    elif val =='b2':
        print((b-n)*a)
    elif val == 'a1':
        print(x*(b-(n-(a-x))))
    else:
        print(y*(a-(n-(b-y))))