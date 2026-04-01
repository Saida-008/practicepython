s = input()

# очистка
s = s.lower().replace(" ", "")

# проверка
print(s == s[::-1])
