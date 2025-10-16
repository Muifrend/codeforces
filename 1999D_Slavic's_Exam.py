for _ in range(int(input())):
    f = input()
    s = input()
    counter = 0
    for i in range(len(f)-1,-1,-1):
        if counter == len(s):
            break
        if f[i]==s[counter]:
            counter+=1
        elif f[i] == '?':
            f = f.replace('?', s[counter], 1)
            counter+=1

    if counter == len(s):
        print('Yes')
        print(f.replace('?','a'))
    else:
        print('No')