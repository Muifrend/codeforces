n = int(input())
y = sorted(list(map(int, input().split())))
string = ' '.join(str(num) for num in y)
print(string)