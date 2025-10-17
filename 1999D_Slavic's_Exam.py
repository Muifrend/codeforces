for _ in range(int(input())):
    f = list(input())
    s = "".join(reversed(input()))
    counter = 0
    for i in range(len(f)-1,-1,-1):
        if counter == len(s):
            break
        if f[i] == '?':
            f[i] = s[counter]
            counter+=1
        elif f[i]==s[counter]:
            counter+=1
    ff = "".join(f)
    if counter == len(s):
        print('Yes')
        print(ff.replace('?','a'))
    else:
        print('No')