text = input()
uppercase_count = sum(1 for char in text if char.isupper())
lowercase_count = sum(1 for char in text if char.islower())
if uppercase_count>lowercase_count:
    print(text.upper())
else:
    print(text.lower())