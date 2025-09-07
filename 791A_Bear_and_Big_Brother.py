bears = input().split()
limakWeight = int(bears[0])
bobWeight = int(bears[1])
counter = 0
while not limakWeight > bobWeight:
    counter += 1 
    limakWeight *= 3
    bobWeight *= 2
print(counter)