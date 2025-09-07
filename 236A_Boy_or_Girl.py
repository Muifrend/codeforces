username = input()
uniqueChars = list(set(sorted(username)))
if len(uniqueChars)%2==1:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')