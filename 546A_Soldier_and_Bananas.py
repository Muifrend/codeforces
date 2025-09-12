numbers = input().split()
price = int(numbers[0])
money = int(numbers[1])
amount = int(numbers[2])
total = 0
for i in range(amount):
    total += (i+1)*price
if total>money:
    print(total-money)
else:
    print(0)