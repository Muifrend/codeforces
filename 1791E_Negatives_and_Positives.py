n = int(input())
for _ in range(n):
    l = int(input())
    a = list(map(int, input().split()))

    positive_nums = list(map(abs, a))
    original_sum = sum(positive_nums)
    negative_count = len([i for i in a if i < 0])

    if negative_count % 2 == 1:
        original_sum -= 2*min(positive_nums)
        
    print(original_sum) 