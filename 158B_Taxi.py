import math
n = input()
array = sorted(input().split())
numOfCars, threes, twos, ones = [array.count(i) for i in ['4','3','2','1']]
for i in range(min(threes, ones)):
        numOfCars += 1
if min(threes, ones) == ones:
    numOfCars += threes - ones
    numOfCars += math.ceil(twos/2)
else:
    ones = abs(threes - ones)
    if twos%2 == 0:
        numOfCars += twos/2
        numOfCars += math.ceil(ones/4)
    else:
        numOfCars += twos//2
        numOfCars += math.ceil((ones+2)/4)
print(int(numOfCars))