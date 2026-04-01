n = int(input())

s = str(n)
power = len(s)

total = 0
for digit in s:
    total += int(digit) ** power

print(total == n)
