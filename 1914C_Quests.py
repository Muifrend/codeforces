n = int(input())
for _ in range(n):
    length, attempts = map(int, input().split())
    clear = list(map(int, input().split()))[:attempts]
    repeat = list(map(int, input().split()))[:attempts-1]

    if attempts<length:
        length = attempts
    
    if attempts == 1:
        high = clear[0]
    else:
        cum, best_repeat = 0, 0
        high = sum(clear) + max(repeat)*(attempts-length)
        for i in range(length):
            cum += clear[i]
            if i < length-1:
                best_repeat = max(best_repeat, repeat[i])
            total = cum + (attempts-1-i) * best_repeat
            if total>high:
                high = total
    print(high)