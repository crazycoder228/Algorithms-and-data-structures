import re

print("Введите первую строку:")
s = input()

print("Введите вторую строку:")
t = input()

matches = re.finditer(t, s)
indexes = [match.start() for match in matches]

if indexes != []:
    print(*indexes) 
else:
    print("Нет вхождений")