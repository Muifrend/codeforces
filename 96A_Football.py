n = input()
k = n.split('1')
y = n.split('0')
zeros = [i for i in k if i]
ones = [l for l in y if l]
longZero = len(max(zeros, key=len))
longOne = len(max(ones, key=len))
print('YES' if longZero > 6 or longOne > 6 else 'NO')