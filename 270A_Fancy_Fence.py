s = int(input())
angles = []
for i in range(3,500):
    angles.append(180*(i-2)/i)
for _ in range(s):
    angle = int(input())
    if angle<180 and angle>59 and angle in angles:
        print('YES')
    else:
        print('NO')